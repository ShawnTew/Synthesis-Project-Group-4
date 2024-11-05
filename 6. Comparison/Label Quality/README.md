 # Labeling and Label Quality
<!-- Qiaorui Yang, Shawn Tew, Xiaduo Zhao, Walter Kahn, Marieke van Arnhem -->

## Abstract
The files in this folder explain how to determine which label should be called which building part and how to calculate the overall accuracy of the label quality.

### Files
- Make sure you have a Gaussian splatted file or point cloud file with clusters. Meaning, they have an attribute such as *cluster*. This attribute column contains integers per point/ splat. The integer represents the cluster it is assigned to.

## Installation
- Step 1:
  - Make sure you have installed BLENDER.
  - Make sure you have installed the IFC add on, see the readme in *5. Visualisation/Blender set up*.
- Step 2 and step 3:
  - Make sure you have created a Python environment that has installed [matplotlib](https://matplotlib.org/stable/install/index.html), [pandas](https://pandas.pydata.org/docs/getting_started/install.html), [numpy](https://numpy.org/install/) and [seaborn](https://pypi.org/project/seaborn/).

## Steps
1. First, calculate per cluster how many points lie in which building part. For this, follow the instructions in *Scripts BLENDER.ipynb* to do this calculation in Blender. Make sure to do the *TO DO* 's.
   - Input: IFC model with building elements, segmented file (either Gaussian splats or point cloud).
   - This creates csv file(s) in the folder *7. Results/Accuracy csv scores*. Per csv file you see per cluster how many points are inside a specific building part.
2. Second, label the clusters: so giving a cluster a label name. Follow the steps in *Add labels.ipynb*. Make sure to do the *TO DO* 's.
   - Input: the csv files of step 1.
   - This creates csv file(s) in the folder *7. Results/labeled.csv*. In the csv file you see per model which cluster is which label.
3. Third, calculate an overall label accuracy by following the steps in *Calculate overall accuracy labels.ipynb*. Make sure to do the *TO DO* 's.
   - Input: labeled.csv from step 2.
   - Output are graphs which are shown in the notebook file.

