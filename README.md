# 3D_STEP-Colorizer-App
An Application For Coloring 3D-Step File (Primarily For Step Files Used in Kicad)
**A short video previewing the App**

https://user-images.githubusercontent.com/23279806/220569250-f296a1ec-e648-43cc-9c2d-67eabe2d61f0.mp4

UPDATE: 3/8/23: Posted the Linux version. Note, as with the Windows version, all works except for the Alpha slider, noted below.

UPDATE 3/5/23: Posted the Windows version (prelim) (filename is: "STEP_Colorizer_Win_hope.zip"

NOTE: The Mac, Linux and Windows .zip contain the Part files.
Backup Part STEP files are in Backup zip.

The posted versions are 99% good as far a I can tell running Linux and Windows in Virtual machines but, I do see some Graphic differences in the layouts (some items seem crowded - perhaps only on a Virtual Machine).
Note: I've added a Slider for setting Alpha Transparency but have Not yet implemented the code to use it.

I will finalize all versions but I'll be looking for comments before posting them
Eventually, I'll sort out the quirks and dial-in consistentancy between OSX, Windows and Linux)

### FYI
These are Preliminary releases of a 3D-STEP file utility, primarily for enhancement-use in conjunction with Kicad's PCB 3D-Viewer.

Although a Stand-Alone App, you can also run the App from the included Kicad Plugin (you'll need to edit the .py (python file) to point to the App's install location and graphic image (png) for logo...(see posted screenshot).

This is Not an official Kicad plugin so, all that's needed is to place the .py file and the .PNG image in the 'kicad/6.0/scripting/plugins' folder.
The plugin will run the app from the installed location.



### App: STEP_Colorizer
Version:  v1r0 **(PRELIM)**
Author: Bruce T.   Kicad Username:  'blackcoffee'
Files Posted At: Here at Github

### CONTENTS:
•Description
•Installing
•Using
•Tip's

### DESCRIPTION:
Colors items in STEP files having their colors previously defined as RGB
values of: '1' for any/all of the 'COLOUR_RGB' strings in the file. The other Colors
in the STEP file will Not be affected.
All of the included 'Stock' STEP files already contain the appropriate declarations.

### INSTALLING:
**Helpful Info Prior to Installation**
Download the STEP_Colorizer(for your system). It contains all the files.

There is a Backup Folder containing the included STEP files.
The App (.zip) contains a Selection of Stock-Parts provided for Ease-Of-Use.

To be able to select them from the Drop-Down 'Part Selector', they **MUST** be
located in the SAME FOLDER as the App.

However, if you prefer a different location, that's O.K., but you will NOT
be able to Select them from the Drop-Down (more info in 'Using' Section).

Install the App (and files) - it is a 'Stand-Alone' application that can also
be run from a Kicad Plugin ( .py also provided for download).
The Plugin will need EDITing of the App file location...

### USING:
Select a Part
Select desired Colors including Tan/Blue Resistor Body Color
Save New Step
Done!

If you installed into location without also installing the Parts into the same
location, simply Select the 'Select Part' in Drop-Down, you will be Prompted
to locate a STEP file.

Note: Selecting 'Select Part' is a User's tool for changing Colors on STEP files
for testing, including the many STEP files provided by Kicad and elsewhere.
Thus, use with Caution as you many corrupt a good STEP file. Make a Backup!
Also, you can have Both the included Parts and also Select Part from other
other locations.

**Note:** All files are Saved to the App's location.

### TIP's:
See Examples of changing color on non-included STEP files.

Learn to add the STEP file to your Footprint and how to properly take
advantage of Kicad' ability to setup multiple 3D-Models (STEP files) for
a Footprint and how to Update PCB with/without affecting particular/all
Footprints
