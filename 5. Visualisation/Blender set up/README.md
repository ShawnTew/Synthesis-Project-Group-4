# Blender setup
<!-- Qiaorui Yang, Shawn Tew, Xiaduo Zhao, Walter Kahn, Marieke van Arnhem -->
![image](../../assets/BlenderHeaderImage.png)

## Abstract

Blender is a free opensource 3D modelling and rendering program that allows the user to import a large variety of data types including IFC, Gaussian splats and 3D point clouds. It was used in the project to compare the segmented results.


<!-- Hi Walter, marieke writing here. I added one notebook file to your folder. In this you can find the scripts i have used in blender.
Aso, there is a zip file. Since the add on for gaussian splats (https://github.com/ReshotAI/gaussian-splatting-blender-addon) did not import the cluster name for the gaussian splats when importing a gaussian splat, I changed the code so it was possible to see the cluster per gaussian splat.
Because before, the whole column was not visible in blender so showing the cluters was not possible. -->

<!-- Also make sure how to tell how to upload an IFC model into blender. -->

<!-- And how to visualise clusters individually in blender for a gaussian splatted file. Make sure to import the add on I have added to this folder. -->

### Software Requirements
- Blender 4.2 or later
- Blender Add-on Bonsai
- Blender Add-on Gaussian splatting Blender Addon originally by ReshotAI slightly adjusted to allow for the visualisation of the 

### Files
- Gaussian splatted .ply file from step 3
- IFC model in .ifc
- Pointcloud in .ply


## Installation

Here is the explanation on how to install the three different addon's needed

### Gaussian splat in Blender

For the installation of the Gaussian splat tool which is based on ReshotAI. The add-on has been slightly changed.

Download the included zip file

Open Blender 

Go to the ribbon tab "edit" and click on the option "Preferences" or press Ctrl , to open the preferences menu.

Go to "Get Extensions"

If this is the first time in this menu allow to search for global searching of extensions

Press the down arrow in the top right corner of the preferences and click on "Install from disk"

Navigate towards the location of the downloaded repository and click on "install from Disk" in the bottom right.

### IFC models in Blender

For the installation of the Gaussian splat tool which is based on ReshotAI. The add-on has been slightly changed.

Open Blender 

Go to the ribbon tab "edit" and click on the option "Preferences" or press Ctrl , to open the preferences menu.

Go to "Get Extensions"

If this is the first time in this menu allow to search for global searching of extensions

Use "Search Extensions" and look for "Bonsai" click on install now the plug-in is installed. 

## Steps

This explains the steps for setting up the Blender process for the three different data types.

### Gaussian splat in Blender

Open Blender

Remove all objects from the standard file

Open the transform menu by pressing n

On the right side of the viewport a list of menu's opens

Click on the one called "3D Gaussian Splatting"

Click on the "Import Gaussian Splatting" button

navigate to the location of the splatted .ply file

On the screen a cloud of diamonds will appear these are the splats

To visualize the splats as elipses change the "As point cloud (faster)" button to off

Switch the rendering mode to Viewport Shading

Now the gaussian splat is imported the correct colors take a while to load.

[![Video 1](https://img.youtube.com/vi/gr_CM2CnTuo/0.jpg)](https://youtu.be/gr_CM2CnTuo)

### IFC models in Blender

Open Blender

Remove all object from the standard file

Go to File -> Open IFC project

navigate to the location of the .ifc file
 
press "Load project"

The .ifc model should now appear on screen

[![Video 2](https://img.youtube.com/vi/7XUUwbv6eHw/0.jpg)](https://www.youtube.com/watch?v=7XUUwbv6eHw)
### Point clouds in Blender 

For the point cloud we use the method described by Florent Poux in https://www.youtube.com/watch?v=DCkFhHNeSc0&t=630s specifically 4,5 and with a slightly different set-up for setting up the lighting.

Open Blender

Remove all objects from the standard file

Go to File -> Import -> Stanford PLY (.ply)

This opens a explorer window

navigate to the location of the .ply file

press IMPORT PLY

now the pointcloud is imported as a collection of vertexes

Click on the vertexes and change the timeline at the bottom to a Shader Editor and make a new Shader Give it a discriptive name

Press Shift-A to add a new node

In the search bar look for the "Attribute" Node

Connect the Attribute Color with the BaseColor of the Principled BDSF

Also open the Emission tab on the Principle BDSF and connect the Attribute Color to the Emission Color and set the strenght to 2.0.

The reason for this choice is that it will remove the need for a light to be placed in the scene which can cause incorrect shading

In the Attribute Node fill in "COL" in the Attribute name this tells Blender that you want to use the color column for each point in the PLY.

Now change the Shader Editor to a Geometry node Editor

Add a new geometry node group

Using Shift-A we need to add two geometry nodes. Similair to before use the search feature and look for "MeshtoPoints" and "Set Material" connect these as shown in the video

Set the radius of the points to 0.01 meter and set your created material in "Set Material"

Now the process has been set up and the user can change the Viewport to "Viewport Shading". 

Open the options for the Shading and turn of the "Scene Light" and "Scene World". Now the point cloud blender setup has been completed.

[![Video 3](https://img.youtube.com/vi/H_8cY9wxN3c/0.jpg)](https://www.youtube.com/watch?v=H_8cY9wxN3c)


[site](https://github.com/ShawnTew/Synthesis-Project-Group-4)

