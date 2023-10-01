# BODY SOUND
”Body Sound” is a project whose aim is to develop a virtual musical instrument for an artistic installation.<br/><br/>
It can be used by an artist in order to make his performance more appealing thanks to the graphic visualization, but it can also have educational purposes to teach the sounds of the different grades of the scale.<br/><br/>
The system uses a sensor (camera) that receives information from the external real environment and then a visual representation reacts to the inputs given by showing a graphic representation on a screen and playing some sounds.

<p align="center">
<img src="style/img/Keyboard.jpeg" alt="keyboard" width="1200"/>
</p>

## Installation
Download this repository and all the specific software:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Max8](https://cycling74.com/downloads)
* [TouchDesigner](https://derivative.ca/UserGuide/Install_TouchDesigner)

Download all the required libraries by running on the Visual Studio Code terminal:
```bash
pip install -r .\requirements.txt
```

In order to use in particular the Magenta library you have to use Python version: 3.7.9
In order to use the software it is suggested to use different machines for performance and computational issues.
You can set up the communication between devices via OSC protocol communications.

Open all the files in their dedicated programs and run them contemporarily since it is a real-time project:
* *NonnoNanni* file with Visual Studio Code (it is better to run it exclusively on a single device)
* *body_main.py* file with Visual Studio Code
* *Ciaone* file with Max8
* *CeLaFaremo* file with TouchDesigner
  
## How to use
Qui inseriremo delle istruzioni generali una volta fatte le mappature.

## Video demo and Report

A video demonstration of the project is available at this [link](https://www.youtube.com/).<br></br>
A brief pdf report of the project is available at this [link](https://github.com/andrewbertax96/ACTAM-Synth/blob/main/presentation/ACTAM___Subtractive_Synthesizer.pdf).

###
This application was developed as a project for the "Creative Programming & Computing" course at [Politecnico di Milano](https://www.polimi.it) (MSc in Music and Acoustic Engineering).
