import sys
import pcbnew
import os
import subprocess
import wx

pcbnew.GetBoard()
from pcbnew import *

class SimplePlugin(pcbnew.ActionPlugin):
    
    def defaults(self):
        self.name = "STEP_Colorizer"
        self.category = "PCB_Parts"
        self.description = "STEP_Color_Changer"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'k_STEPcolor.png') # Optional, defaults to ""

    def Run(self):
        pass  # a Null command until there's executable code here...
  # This next line works from Kicad!!!!!! plugin
        subprocess.call(['/usr/bin/open','/Users/bruce/dist/Step_Colorizers/STEP_Colorizer_v1r0_MAC_Pre.app'])

SimplePlugin().register() # Instantiate and register to Pcbnew

