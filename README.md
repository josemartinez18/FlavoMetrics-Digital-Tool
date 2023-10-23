# Flavometrics-Digital-Tool
![Flavometrics Main Image](<Images/FlavoMetrics Tool.jpg>)
Open source biodesign digital tool from the ACM Designing Interactive Systems 2023 pictorial ["FlavoMetrics: Towards a Digital Tool to Understand and Tune Living Aesthetics of Flavobacteria"](https://dl.acm.org/doi/10.1145/3563657.3596085). 

Authors: Clarice Risseeuw, Jose Francisco Martinez Castro, Pascal Barla, Elvin Karana

[DIS 2023 Preview Video](https://www.youtube.com/watch?v=oMSLKfJZpuI)

# Installation
Currently only supported on Windows.

## Using Standalone App

1. Open the "Flavometrics Standalone App" folder.
2. Click and run "FlavometricsApp.exe"
3. Now you are ready to use the tool and tune the living aesthetics of Flavobacteria!

## Using Source Blender Files

1. Downloadoad the latest version of UPBGE: https://upbge.org
2. Download all files in the github repository
3. Open the .blend file
4. Under Edit > Preferences > Add-ons, search for Logic Nodes. Enable Logic Nodes by clicking on the checkbox and click on "Install or Update Uplogic Module". Wait for the innstallation to complete before continuing.
![Enabling Logic Nodes](<Images/Enable Logic Nodes.png>)
5. To run the app from UPBGE, In the "Layout" window, select "Render Properties" on the right hand menu (camera icon). At the top, you have the option for an "Embedded Start" (launching the tool in the Blender window) or "Standalone Start" (launching the tool in its own independent window)
![Launching Flavometrics](<Images/Launching Flavometrics.png>)

Note: Updates to the UPBGE software and the Logic Nodes add-on can sometimes make certain features of the Flavometrics tool incompatible. if this is the case when running the tool using the Source Blender Files, make sure to try the Standalone app as an alternative.

# FAQ
1. How can I improve the performance of the tool when running on the computer?
    
    The tool uses CPU (Eevee renderer) to render the textures. Depending on your PC configuration, it is recommended to lower the display resolution of your PC display to improve performance. Running the tool at 720p has a significant performance boost compared to 1080p. 

    Additionally, you can adjust the resolution of the digital tool below the "Embedded Start" button.

2. Can the Flavometrics tool run on Mac?

    Unfortunately, the limitations of the Blender Mac app do not enable the tool to run fully on Mac. As the implementation of the tool uses about 20 BRDF images to capture a full representation of Flavobacteria, the Blender Eevee render engine for Mac reaches a bottle neck (maximun around 8 images). More information can be found here: https://projects.blender.org/blender/blender/issues/88157
