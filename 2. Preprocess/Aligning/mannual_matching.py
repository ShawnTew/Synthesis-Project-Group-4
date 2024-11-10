import open3d as o3d
import numpy as np
import copy
from plyfile import PlyData, PlyElement
import laspy

# Define PLY and LAS file paths
geoslam_ply_path = "D:/GEO1101_Synthesisproject/labeled_point_cloudtest2(PLY)- Cloud.ply"
polycam_ply_path = "D:/GEO1101_Synthesisproject/SPLAT_PLY_bouwpub_cropped_inBlender.ply"
bouwpub_ply_path = "D:/GEO1101_Synthesisproject/bouwpub.ply"  # Assuming bouwpub point cloud file path

# Paths to additional point cloud files
colored_las_path = "D:/GEO1101_Synthesisproject/colored_point_cloud (final222).las"
cluster_GM5_ply_path = "D:/GEO1101_Synthesisproject/alignplease/cluster_GM5.ply"
cluster_GM13_ply_path = "D:/GEO1101_Synthesisproject/alignplease/cluster_GM13.ply"
cluster_GM20_ply_path = "D:/GEO1101_Synthesisproject/alignplease/cluster_GM20.ply"
cluster_kMeans4_ply_path = "D:/GEO1101_Synthesisproject/alignplease/cluster_kMeans4.ply"
cluster_kMeans10_ply_path = "D:/GEO1101_Synthesisproject/alignplease/cluster_kMeans10.ply"


# Function to load PLY using plyfile and extract all properties and comments
def load_ply_with_attributes(ply_path, name="PointCloud"):
    try:
        ply = PlyData.read(ply_path)
        vertex = ply['vertex']
        data = {}
        for prop in vertex.properties:
            data[prop.name] = vertex[prop.name]

        # Extract comments from the header
        comments = ply.comments if 'comments' in ply.header else []

        # Convert to Open3D PointCloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(np.vstack((data['x'], data['y'], data['z'])).T)

        # Assign colors if present
        if 'red' in data and 'green' in data and 'blue' in data:
            colors = np.vstack((data['red'], data['green'], data['blue'])).T / 255.0
            pcd.colors = o3d.utility.Vector3dVector(colors)

        # Assign normals if present
        if 'nx' in data and 'ny' in data and 'nz' in data:
            normals = np.vstack((data['nx'], data['ny'], data['nz'])).T
            pcd.normals = o3d.utility.Vector3dVector(normals)

        print(f"Loaded {name}: {len(pcd.points)} points with attributes")
        return pcd, data, comments
    except MemoryError:
        print(f"MemoryError: Unable to load {name} from {ply_path}. Consider downsampling the point cloud.")
        return None, None, None
    except Exception as e:
        print(f"Error loading {name} from {ply_path}: {e}")
        return None, None, None


# Function to load LAS file using laspy and extract all properties
def load_las_with_attributes(las_path, name="PointCloud"):
    try:
        las = laspy.read(las_path)
        data = {}
        data['x'] = las.x
        data['y'] = las.y
        data['z'] = las.z

        # Get attributes (standard and extra dimensions)
        for dim_name in las.point_format.dimension_names:
            if dim_name not in ['X', 'Y', 'Z']:
                data[dim_name] = getattr(las, dim_name)

        # Convert to Open3D PointCloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(np.vstack((data['x'], data['y'], data['z'])).T)

        # Assign colors if present
        if 'red' in data and 'green' in data and 'blue' in data:
            colors = np.vstack((data['red'], data['green'], data['blue'])).T / 65535.0  # LAS colors are usually 16-bit
            pcd.colors = o3d.utility.Vector3dVector(colors)

        print(f"Loaded {name}: {len(pcd.points)} points with attributes")
        return pcd, data, []
    except MemoryError:
        print(f"MemoryError: Unable to load {name} from {las_path}. Consider downsampling the point cloud.")
        return None, None, None
    except Exception as e:
        print(f"Error loading {name} from {las_path}: {e}")
        return None, None, None


# Function to save PLY with all original attributes and comments
def save_ply_with_attributes(ply_path, pcd, original_data, original_comments):
    try:
        # Prepare data for PlyElement
        num_points = len(pcd.points)
        vertex_data = {
            'x': np.asarray(pcd.points)[:, 0],
            'y': np.asarray(pcd.points)[:, 1],
            'z': np.asarray(pcd.points)[:, 2]
        }

        if pcd.has_colors():
            vertex_data['red'] = (np.asarray(pcd.colors)[:, 0] * 255).astype(np.uint8)
            vertex_data['green'] = (np.asarray(pcd.colors)[:, 1] * 255).astype(np.uint8)
            vertex_data['blue'] = (np.asarray(pcd.colors)[:, 2] * 255).astype(np.uint8)

        if pcd.has_normals():
            vertex_data['nx'] = np.asarray(pcd.normals)[:, 0]
            vertex_data['ny'] = np.asarray(pcd.normals)[:, 1]
            vertex_data['nz'] = np.asarray(pcd.normals)[:, 2]

        # Add any additional attributes from original data
        for key in original_data:
            if key not in vertex_data and key not in ['x', 'y', 'z', 'nx', 'ny', 'nz', 'red', 'green', 'blue']:
                vertex_data[key] = original_data[key]

        # Create structured array
        dtype = []
        for key in vertex_data:
            if key in ['red', 'green', 'blue']:
                dtype.append((key, 'u1'))
            elif key.startswith('cov_'):
                dtype.append((key, 'f4'))
            else:
                dtype.append((key, 'f4'))
        vertex = np.empty(num_points, dtype=dtype)
        for key in vertex_data:
            vertex[key] = vertex_data[key]

        # Create PlyElement
        el = PlyElement.describe(vertex, 'vertex')

        # Prepare PlyData with comments
        ply_out = PlyData([el], text=True, comments=original_comments)

        # Save PLY
        ply_out.write(ply_path)
        print(f"Saved point cloud with attributes to {ply_path}")
    except Exception as e:
        print(f"Error saving point cloud to {ply_path}: {e}")


# Function to print all attributes to the console
def print_attributes(name, data):
    print(f"\nAttributes for {name}:")
    for key in data:
        print(f"  {key}:")
        # Print first 5 values for brevity
        sample_values = data[key][:5]
        print(f"    Sample values: {sample_values}")
    print("\n" + "-" * 50)


# Load all point clouds with attributes and comments
geoslam_pcd_original, geoslam_data, geoslam_comments = load_ply_with_attributes(geoslam_ply_path, "Geoslam")
polycam_pcd_original, polycam_data, polycam_comments = load_ply_with_attributes(polycam_ply_path, "Polycam")
bouwpub_pcd_original, bouwpub_data, bouwpub_comments = load_ply_with_attributes(bouwpub_ply_path, "Bouwpub")

# Load additional point clouds
colored_pcd_original, colored_data, colored_comments = load_las_with_attributes(colored_las_path, "Colored LAS")
cluster_GM5_pcd_original, cluster_GM5_data, cluster_GM5_comments = load_ply_with_attributes(cluster_GM5_ply_path,
                                                                                            "Cluster GM5")
cluster_GM13_pcd_original, cluster_GM13_data, cluster_GM13_comments = load_ply_with_attributes(cluster_GM13_ply_path,
                                                                                               "Cluster GM13")
cluster_GM20_pcd_original, cluster_GM20_data, cluster_GM20_comments = load_ply_with_attributes(cluster_GM20_ply_path,
                                                                                               "Cluster GM20")
cluster_kMeans4_pcd_original, cluster_kMeans4_data, cluster_kMeans4_comments = load_ply_with_attributes(
    cluster_kMeans4_ply_path, "Cluster kMeans4")
cluster_kMeans10_pcd_original, cluster_kMeans10_data, cluster_kMeans10_comments = load_ply_with_attributes(
    cluster_kMeans10_ply_path, "Cluster kMeans10")

# Ensure all point clouds are loaded successfully
if any(pcd is None for pcd in [geoslam_pcd_original, polycam_pcd_original, bouwpub_pcd_original,
                               colored_pcd_original, cluster_GM5_pcd_original, cluster_GM13_pcd_original,
                               cluster_GM20_pcd_original, cluster_kMeans4_pcd_original, cluster_kMeans10_pcd_original]):
    print("Error loading point clouds. Exiting.")
    exit(1)

# Create copies of point clouds for transformation
geoslam_pcd = copy.deepcopy(geoslam_pcd_original)
polycam_pcd = copy.deepcopy(polycam_pcd_original)
bouwpub_pcd = copy.deepcopy(bouwpub_pcd_original)
colored_pcd = copy.deepcopy(colored_pcd_original)
cluster_GM5_pcd = copy.deepcopy(cluster_GM5_pcd_original)
cluster_GM13_pcd = copy.deepcopy(cluster_GM13_pcd_original)
cluster_GM20_pcd = copy.deepcopy(cluster_GM20_pcd_original)
cluster_kMeans4_pcd = copy.deepcopy(cluster_kMeans4_pcd_original)
cluster_kMeans10_pcd = copy.deepcopy(cluster_kMeans10_pcd_original)

# Define corresponding points
# Please adjust the coordinates of corresponding points based on actual situation, ensuring they accurately correspond in each point cloud

# For geoslam_pcd
geoslam_points = np.array([
    [5.07, 4.86, 2.8],  # A
    [11.86, 5.06, 6.45],  # B
    [0.66, 4.72, 6.45],  # C
    [7.36, 4.86, 2.8],  # D
])

# For polycam_pcd
polycam_points = np.array([
    [0.926237, -5.12686, -3.40671],  # A
    [8.43343, -9.52554, -0.794369],  # B
    [-3.74852, -9.57356, -5.88085],  # C
    [3.56126, -5.11336, -2.28221],  # D
])

# For bouwpub_pcd (IFC target)
bouwpub_points = np.array([
    [-0.244364, -1.58571, 3.64124],  # A
    [6.66806, -1.62656, 7.30621],  # B
    [-4.77633, -1.62656, 7.30621],  # C
    [2.14446, -1.58571, 3.64124],  # D
])

# For colored_pcd
colored_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],
])

# For cluster_GM5_pcd
cluster_GM5_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],


])

# For cluster_GM13_pcd
cluster_GM13_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],
])

# For cluster_GM20_pcd
cluster_GM20_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],
])

# For cluster_kMeans4_pcd
cluster_kMeans4_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],
])

# For cluster_kMeans10_pcd
cluster_kMeans10_points = np.array([
    [5.0653, 4.8623, 2.7973],
    [11.856, 5.058, 6.4523],
    [0.6489, 4.714, 6.424],
    [7.8936, 4.9487, 2.7895],
])

# Corresponding points in bouwpub_pcd for the above point clouds
bouwpub_points_for_colored = np.array([
    [-0.244364, -1.58571, 3.64124],  # A
    [6.66806, -1.62656, 7.30621],  # B
    [-4.77633, -1.62656, 7.30621],  # C
    [2.14446, -1.58571, 3.64124],  # D
])

# For other cluster point clouds, you can use the same bouwpub_points_for_colored
bouwpub_points_for_cluster_GM5 = bouwpub_points_for_colored.copy()
bouwpub_points_for_cluster_GM13 = bouwpub_points_for_colored.copy()
bouwpub_points_for_cluster_GM20 = bouwpub_points_for_colored.copy()
bouwpub_points_for_cluster_kMeans4 = bouwpub_points_for_colored.copy()
bouwpub_points_for_cluster_kMeans10 = bouwpub_points_for_colored.copy()


# Compute transformation matrix (including rotation, scaling, and translation)
def compute_transformation(source_points, target_points, allow_scale=True):
    # Step 1: Compute centroids
    centroid_source = np.mean(source_points, axis=0)
    centroid_target = np.mean(target_points, axis=0)

    # Step 2: Center the points
    source_centered = source_points - centroid_source
    target_centered = target_points - centroid_target

    # Step 3: Compute the covariance matrix
    H = np.dot(source_centered.T, target_centered)

    # Step 4: Perform Singular Value Decomposition
    U, S, Vt = np.linalg.svd(H)

    # Step 5: Calculate the rotation matrix
    R = np.dot(Vt.T, U.T)

    # Ensure a right-handed coordinate system
    if np.linalg.det(R) < 0:
        Vt[2, :] *= -1
        R = np.dot(Vt.T, U.T)

    # Step 6: Calculate the scaling factor (if scaling is allowed)
    if allow_scale:
        scale_factor = np.sum(S) / np.sum(np.linalg.norm(source_centered, axis=1) ** 2)
    else:
        scale_factor = 1.0

    # Step 7: Calculate the translation vector
    t = centroid_target - scale_factor * np.dot(R, centroid_source)

    # Step 8: Create the transformation matrix (including scaling)
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, :3] = scale_factor * R
    transformation_matrix[:3, 3] = t

    return transformation_matrix


# Compute transformation matrices
transformation_geoslam_to_bouwpub = compute_transformation(geoslam_points, bouwpub_points, allow_scale=True)
print("\nTransformation matrix (Geoslam -> Bouwpub):\n", transformation_geoslam_to_bouwpub)

transformation_polycam_to_bouwpub = compute_transformation(polycam_points, bouwpub_points, allow_scale=True)
print("\nTransformation matrix (Polycam -> Bouwpub):\n", transformation_polycam_to_bouwpub)

# For colored_pcd
if colored_points.size > 0:
    transformation_colored_to_bouwpub = compute_transformation(colored_points, bouwpub_points_for_colored,
                                                               allow_scale=True)
    print("\nTransformation matrix (Colored LAS -> Bouwpub):\n", transformation_colored_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Colored LAS point cloud.")

# For cluster_GM5_pcd
if cluster_GM5_points.size > 0:
    transformation_cluster_GM5_to_bouwpub = compute_transformation(cluster_GM5_points, bouwpub_points_for_cluster_GM5,
                                                                   allow_scale=True)
    print("\nTransformation matrix (Cluster GM5 -> Bouwpub):\n", transformation_cluster_GM5_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Cluster GM5 point cloud.")

# For cluster_GM13_pcd
if cluster_GM13_points.size > 0:
    transformation_cluster_GM13_to_bouwpub = compute_transformation(cluster_GM13_points,
                                                                    bouwpub_points_for_cluster_GM13, allow_scale=True)
    print("\nTransformation matrix (Cluster GM13 -> Bouwpub):\n", transformation_cluster_GM13_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Cluster GM13 point cloud.")

# For cluster_GM20_pcd
if cluster_GM20_points.size > 0:
    transformation_cluster_GM20_to_bouwpub = compute_transformation(cluster_GM20_points,
                                                                    bouwpub_points_for_cluster_GM20, allow_scale=True)
    print("\nTransformation matrix (Cluster GM20 -> Bouwpub):\n", transformation_cluster_GM20_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Cluster GM20 point cloud.")

# For cluster_kMeans4_pcd
if cluster_kMeans4_points.size > 0:
    transformation_cluster_kMeans4_to_bouwpub = compute_transformation(cluster_kMeans4_points,
                                                                       bouwpub_points_for_cluster_kMeans4,
                                                                       allow_scale=True)
    print("\nTransformation matrix (Cluster kMeans4 -> Bouwpub):\n", transformation_cluster_kMeans4_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Cluster kMeans4 point cloud.")

# For cluster_kMeans10_pcd
if cluster_kMeans10_points.size > 0:
    transformation_cluster_kMeans10_to_bouwpub = compute_transformation(cluster_kMeans10_points,
                                                                        bouwpub_points_for_cluster_kMeans10,
                                                                        allow_scale=True)
    print("\nTransformation matrix (Cluster kMeans10 -> Bouwpub):\n", transformation_cluster_kMeans10_to_bouwpub)
else:
    print("\nPlease provide corresponding points for Cluster kMeans10 point cloud.")

# Apply transformations
geoslam_pcd.transform(transformation_geoslam_to_bouwpub)
polycam_pcd.transform(transformation_polycam_to_bouwpub)
if colored_points.size > 0:
    colored_pcd.transform(transformation_colored_to_bouwpub)
if cluster_GM5_points.size > 0:
    cluster_GM5_pcd.transform(transformation_cluster_GM5_to_bouwpub)
if cluster_GM13_points.size > 0:
    cluster_GM13_pcd.transform(transformation_cluster_GM13_to_bouwpub)
if cluster_GM20_points.size > 0:
    cluster_GM20_pcd.transform(transformation_cluster_GM20_to_bouwpub)
if cluster_kMeans4_points.size > 0:
    cluster_kMeans4_pcd.transform(transformation_cluster_kMeans4_to_bouwpub)
if cluster_kMeans10_points.size > 0:
    cluster_kMeans10_pcd.transform(transformation_cluster_kMeans10_to_bouwpub)

# Assign different colors to point clouds for visualization
bouwpub_pcd.paint_uniform_color([0, 0, 1])  # Blue
geoslam_pcd.paint_uniform_color([1, 0, 0])  # Red
polycam_pcd.paint_uniform_color([0, 1, 0])  # Green
colored_pcd.paint_uniform_color([1, 1, 0])  # Yellow
cluster_GM5_pcd.paint_uniform_color([1, 0, 1])  # Magenta
cluster_GM13_pcd.paint_uniform_color([0, 1, 1])  # Cyan
cluster_GM20_pcd.paint_uniform_color([0.5, 0.5, 0])  # Olive
cluster_kMeans4_pcd.paint_uniform_color([0.5, 0, 0.5])  # Purple
cluster_kMeans10_pcd.paint_uniform_color([0, 0.5, 0.5])  # Teal

# Visualize all point clouds
o3d.visualization.draw_geometries(
    [bouwpub_pcd, geoslam_pcd, polycam_pcd, colored_pcd, cluster_GM5_pcd,
     cluster_GM13_pcd, cluster_GM20_pcd, cluster_kMeans4_pcd, cluster_kMeans10_pcd],
    window_name="Aligned Point Clouds",
    width=800,
    height=600,
    left=50,
    top=50,
    point_show_normal=False
)


# Function to save transformed PLY with all attributes and comments
def save_transformed_ply(original_data, transformed_pcd, original_comments, save_path):
    save_ply_with_attributes(save_path, transformed_pcd, original_data, original_comments)


# Save aligned point clouds separately with all attributes and comments
aligned_geoslam_path = "D:/GEO1101_Synthesisproject/transformed_geoslam_pcd.ply"
save_transformed_ply(geoslam_data, geoslam_pcd, geoslam_comments, aligned_geoslam_path)

aligned_polycam_path = "D:/GEO1101_Synthesisproject/transformed_polycam_pcd.ply"
save_transformed_ply(polycam_data, polycam_pcd, polycam_comments, aligned_polycam_path)

aligned_colored_las_path = "D:/GEO1101_Synthesisproject/transformed_colored_las_pcd.ply"
if colored_points.size > 0:
    save_transformed_ply(colored_data, colored_pcd, colored_comments, aligned_colored_las_path)
else:
    print("Skipping saving transformed Colored LAS point cloud due to missing corresponding points.")

aligned_cluster_GM5_path = "D:/GEO1101_Synthesisproject/transformed_cluster_GM5_pcd.ply"
if cluster_GM5_points.size > 0:
    save_transformed_ply(cluster_GM5_data, cluster_GM5_pcd, cluster_GM5_comments, aligned_cluster_GM5_path)
else:
    print("Skipping saving transformed Cluster GM5 point cloud due to missing corresponding points.")

aligned_cluster_GM13_path = "D:/GEO1101_Synthesisproject/transformed_cluster_GM13_pcd.ply"
if cluster_GM13_points.size > 0:
    save_transformed_ply(cluster_GM13_data, cluster_GM13_pcd, cluster_GM13_comments, aligned_cluster_GM13_path)
else:
    print("Skipping saving transformed Cluster GM13 point cloud due to missing corresponding points.")

aligned_cluster_GM20_path = "D:/GEO1101_Synthesisproject/transformed_cluster_GM20_pcd.ply"
if cluster_GM20_points.size > 0:
    save_transformed_ply(cluster_GM20_data, cluster_GM20_pcd, cluster_GM20_comments, aligned_cluster_GM20_path)
else:
    print("Skipping saving transformed Cluster GM20 point cloud due to missing corresponding points.")

aligned_cluster_kMeans4_path = "D:/GEO1101_Synthesisproject/transformed_cluster_kMeans4_pcd.ply"
if cluster_kMeans4_points.size > 0:
    save_transformed_ply(cluster_kMeans4_data, cluster_kMeans4_pcd, cluster_kMeans4_comments,
                         aligned_cluster_kMeans4_path)
else:
    print("Skipping saving transformed Cluster kMeans4 point cloud due to missing corresponding points.")

aligned_cluster_kMeans10_path = "D:/GEO1101_Synthesisproject/transformed_cluster_kMeans10_pcd.ply"
if cluster_kMeans10_points.size > 0:
    save_transformed_ply(cluster_kMeans10_data, cluster_kMeans10_pcd, cluster_kMeans10_comments,
                         aligned_cluster_kMeans10_path)
else:
    print("Skipping saving transformed Cluster kMeans10 point cloud due to missing corresponding points.")

# Optionally: Save Bouwpub point cloud (unaligned) with all attributes and comments
aligned_bouwpub_path = "D:/GEO1101_Synthesisproject/unaligned_bouwpub_pcd.ply"
save_transformed_ply(bouwpub_data, bouwpub_pcd, bouwpub_comments, aligned_bouwpub_path)
