# Flavometrics-Digital-Tool
![Flavometrics Main Image](<Images/FlavoMetrics Tool.jpg>)
Open source biodesign digital tool from the ACM Designing Interactive Systems 2023 pictorial ["FlavoMetrics: Towards a Digital Tool to Understand and Tune Living Aesthetics of Flavobacteria"](https://dl.acm.org/doi/10.1145/3563657.3596085.). 

Authors:  
Clarice Risseeuw, Jose Francisco Martinez Castro, Pascal Barla, Elvin Karana

[DIS 2023 Preview Video](https://www.youtube.com/watch?v=oMSLKfJZpuI)

# Installation
Currently only supported on Windows.

1. Downloadoad the latest version of UPBGE: https://upbge.org
2. Download all files in the github repository
3. Open the .blend file
4. Under Edit > Preferences > Add-ons, search for Logic Nodes. Enable Logic Nodes by clicking on the checkbox and click on "Install or Update Uplogic Module". Wait for the innstallation to complete before continuing.
![Enabling Logic Nodes](<Images/Enable Logic Nodes.png>)
5. In the "Layout" window, select "Render Properties" on the right hand menu (camera icon). At the top, you have the option for an "Embedded Start" (launching the tool in the Blender window) or "Standalone Start" (launching the tool in its own independent window)
![Launching Flavometrics](<Images/Launching Flavometrics.png>)
6. Now you aree ready to use the tool and tune the living aesthetics of Flavobacteria.

# FAQ
1. How can I improve the performance of the tool when running on the computer?
    
    The tool uses CPU (Eevee renderer) to render the textures. Depending on your PC configuration, it is recommended to lower the display resolution of your PC display to improve performance. Running the tool at 720p has a significant performance boost compared to 1080p. 

    Additionally, you can adjust the resolution of the digital tool below the "Embedded Start" button.
