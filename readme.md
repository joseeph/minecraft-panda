### Project brif

Project Minecraft-panda is an education and research project which is a combination of physical Robotic and minecraft simulation. The idea is like the movie Inside out, there is a brainless Panda, we let kids to act like panda's brain in order to control the panda collectively.

The project is done by Joseph and Mark in FACT Gallary, Liverpool.

### Reference

[RF-Craft](https://github.com/cheapjack/RF-Craft)by Ross was the main reference of this project, we mainly using the python library called [MC-PI](https://github.com/martinohanlon/mcpi) to do the minecraft coding.

### Architecture
![Image](..img/Minecraft Panda.003.jpeg)
![Image](..img/Minecraft Panda.006.jpeg)

like the photo shows, the physical Robotic Panda it self as the minecraft server, the server serves the huge virtual panda, the interesting thing is that it is kind of the real inside out, once you getting into the physical panda.

### Hardware building
- Py2go Robotic
- 2x 9G servo motor
- 3D print Panda(in folder 3dPrintPandaFile)

### How to use
- Place the folder worldPandaLand into minecraft's world folder and replace the original world.
- Open the Minecraft and hit crate new world, flying around the world you should see the huge panda, go to panda's head and mark the position that shows on the top left screen, open the code startGame.py change the pos with your marked figure.
- set up RPI to AP mode

```
cd PNP_RPI3_AP
sudo chmod+x install.sh
sudo ./install.sh
//once the install down
sudo chmod+x ap.sh
sudo ./ap.sh apname appassward
```

- In terminal cd into the minecraft-panda project and 

```
python startGame.py
```

- try hit the diamond block and see the panda move


