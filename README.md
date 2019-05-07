# addandzoom
QGIS Plugin 'addandzoom', made to streamline a cumbersome workflow. 
A demo can viewed in the projects section at http://samkguerrero.com/

1)
The script for the 'addandzoom' plugin must be saved in the plugins folders specified below. 

Windows)
C:\Program Files\apps\qgis\python\plugins\

Mac)
/Applications/QGIS.app/Contents/Resources/python/plugins


2)
Both the County_Index and the Tiger roads folder must be inside the 'addandzoom' folder in the plugins folder for the plugin to work.
Download the County_Index polygon shapefile and Tiger Roads shapefiles.
https://www.dropbox.com/sh/26in0woyx1ilxri/AACrCCTgktgXycMKYkFdyDQPa?dl=0

3)
The plugin is experimental so in order for it to appear as a plugin that can be installed/activated the; 
'show also experimental plugins' box must be checked,
'show also deprecated plugins' box must be checked,

4)
It should appear in the 'Not installed' list where it can then be installed. Once installed, be sure the box to the left is checked
so that it is activated. It will appear in the toolbar. 

In a previous job I was tasked with investigating the roads around specific points at a detailed scale. The workflow consisted of importing Tiger 2015 road shapefiles into QGIS. Followed by zooming to the specified coordinates to inquire about the nearby roads. Loading one at a time was not practical, given that there were multiple coordinates to be searched. I built this plugin using templates online to help streamline the process.The tool's functionality is limited becuase it was design to streamline a specific workflow.

5)
Activate the Python Console.
input coordinates;
Format: latitude/longitude
i.e.
(39.72285,-104.89737),
(40.65272,-73.67761),
(32.39449,-99.74001), 
(41.64252, -87.96293)
