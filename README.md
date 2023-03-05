# 3D_STEP-Colorizer-App
An Application For Coloring 3D-Step File (Primarily For Step Files Used in Kicad)
**A short video previewing the App**

https://user-images.githubusercontent.com/23279806/220569250-f296a1ec-e648-43cc-9c2d-67eabe2d61f0.mp4


UPDATE 3/5/23: Posted the Windows version (prelim) (filename is: "STEP_Colorizer_Win_hope.zip"
The main problem with the Windows version was wxPython/wxWidgets.
I revised the code to use Tkinter Widgets instead of wx... Seems to be working with some odd 'Graphic' differences from the Mac. Otherwise, it's baked well enough for user testing/use.

ALSO NOTE: Both the Mac and Windows .zip contain the Part files. But, for the Windows version, the names of two Jumper Wire have changed: replaced the degree 'symbol' with 'deg'. So, if you need to use them from the zip, just edit the name. I'll clean this up, too...

The previously posted Mac version is working and I'm woking on Linux version.
Note: I've added a Slider for setting Alpha Transparency but have Not yet implemented the code to use it.

I will finalize all versions but I'll be looking for comments before posting them
Eventually, I'll sort out the quirks and dial-in consistentancy between OSX, Windows and Linux)

# FYI
This is a Preliminary release of a 3D-STEP file utility, primarily for enhancement-use in conjunction with Kicad's PCB 3D-Viewer.

The App is currently for Mac-OSX (until I re-install Windows and Linux so I can perform the appropriate testing on those systems and package it).
If you use a Mac, it should install and run without errors.

Although a Stand-Alone App, if using a Mac, you can also run the App from the included Kicad Plugin (you'll need to edit the .py (python file) to point to the App's install location (see posted screenshot).

This is Not an official Kicad plugin so, all that's needed is to place the .py file and the Icon in the 'kicad/6.0/scripting/plugins' folder.
The plugin will run the app from the installed location.



# App: STEP_Colorizer
Version:  v1r0 **(PRELIM)**
Author: Bruce T.   Kicad Username:  'blackcoffee'
Files Posted At: Here at Github

# CONTENTS:
•Description
•Installing
•Using
•Tip's

# DESCRIPTION:
Colors items in STEP files having their colors previously defined as RGB
values of: '1' for any/all of the COLOUR_RGB strings.
All of the included 'Stock' STEP files already contain these declarations.

# INSTALLING:
**Helpful Info Prior to Installation**
Download the STEP_Colorizer_v11r0_ (for your system) Pre.zip

It contains all the files. There is a Backup Folder containing the included STEP files.

The App (.zip) contains a Selection of Stock-Parts provided for Ease-Of-Use.

To be able to select them from the Drop-Down 'Part Selector', they MUST be
located in the SAME FOLDER as the App.

However, if you prefer a different location, that's O.K., but you will NOT
be able to Select them from the Drop-Down (more info in 'Using' Section).

Install the App (and files) - it is a 'Stand-Alone' application that can also
be run from a Kicad Plugin ( .py also provided for download).
The Plugin will need EDITing of the App file location...

# USING:
Select a Part, select desired Colors, Save New Step.

If you installed into location without also installing the Parts into the same
location, simply Select the 'Select Part' in Drop-Down, you will be Prompted
to locate a STEP file.

Note: Selecting 'Select Part' is a User's tool for changing Colors on STEP files
for testing, including the many STEP files provided by Kicad and elsewhere.
Thus, use with Caution as you many corrupt a good STEP file. Make a Backup!
Also, you can have Both the included Parts and also Select Part from other
other locations.

Note: All files are Saved to the App's location.

# TIP's:
See Examples of changing color on non-included STEP files.

Learn to add the STEP file to your Footprint and how to properly take
advantage of Kicad' ability to setup multiple 3D-Models (STEP files) for
a Footprint and how to Update PCB with/without affecting particular/all
Footprints
