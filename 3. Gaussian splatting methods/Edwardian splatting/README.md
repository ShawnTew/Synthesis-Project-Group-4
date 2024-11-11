# Edwardian Splatting setup
<!-- Qiaorui Yang, Shawn Tew, Xiaduo Zhao, Walter Kahn, Marieke van Arnhem -->
![image](assets/name.jpg)

## Abstract
A novel method that was developed during the project was to take the GeoSLAM point cloud place it in blender and take images/ renders as if it were a synthetic model. The resulting Gaussian splat is much denser then purely phone based models.

### Software Requirements
- Blender 4.2 or later
- Blender Add-on Camera Array by Olli Huttunnen can be found at https://toppinappi.gumroad.com/l/Camarray

## Installation
For the installation of the Gaussian splat tool which is based on ReshotAI. The add-on has been slightly changed.

Download the zip file which can be bought here https://toppinappi.gumroad.com/l/Camarray

Open Blender 

Go to the ribbon tab "edit" and click on the option "Preferences" or press Ctrl , to open the preferences menu.

Go to "Get Extensions"

If this is the first time in this menu allow to search for global searching of extensions

Press the down arrow in the top right corner of the preferences and click on "Install from disk"

Navigate towards the location of the downloaded repository and click on "install from Disk" in the bottom right.

## Steps

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

Now for the process of edwardian splatting.

Download the script in the folder and go to the scripting tab of Blender

start a new script and paste the code in the document. Change the location of the csv file which needs to be in the format x;y;z.

Change the size of the cubes but it's recommended to keep it small to allign the sensor location.

Run the code in the scripting tab

All cubes are placed

Go to the layout tab and shift-select all the cubes and join them using Ctrl-j

Open the transform menu by pressing n

On the right side of the viewport a list of menu's opens

Select the joined cubes and press "Create Cameras"

Now press render and all images will be created for the location this takes a while.

[![Video 3](https://img.youtube.com/vi/n7TDKmdYQoU/0.jpg)](https://youtu.be/n7TDKmdYQoU)



[site](https://github.com/ShawnTew/Synthesis-Project-Group-4)

