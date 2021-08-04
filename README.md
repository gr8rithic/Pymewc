# Pymewc ( Python Microcontroller Interface)
## _Making your microcontroller connect with python_

_version:0.0.7.4 Alpha_

 [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
 [![PyPI - License](https://img.shields.io/pypi/l/length)](https://raw.githubusercontent.com/Ratheshprabakar/length/master/LICENSE.md)
![PyPI](https://img.shields.io/pypi/v/pymewc)
[![PyPI downloads](https://img.shields.io/pypi/dm/myfitbit.svg?style=flat)](https://pypi.org/project/pymewc/)
[![Contributions](https://img.shields.io/badge/contributions-welcome-green.svg)](https://img.shields.io/badge/contributions-welcome-green.svg)

- Pymewc is a new and innovative python library that can we used for connecting python with the microcontroller world.
- Pymewc is a lightweight package that aims simplicity yet performing complex tasks with ease.

## Features

- Read data from each pin of the microcontroller
- Read data printed on the serial monitor window
- Scoping Using Analog Pin 0
- Writing program to the microcontroller(Development Stage)
- Sending data to the local cloud service / running a apache server(Development Stage)

## Installation

Pymewc requires [Python](https://www.python.org/) v3.6+ to run.  But extensively tested and recomends using python version > 3.8

Install the dependencies and packages and thats it.

#### For windows
```
pip install pymewc
```
#### For linux and unix based Operating systems

.              
***Downloading pip on linux based operating systems***

Debian and Debian Based distros(Ubuntu, Mint etc)
```
sudo apt install python3-pip
```
For Arch and Arch Based distros(Manjaro, Endevour etc)
```
sudo  pacman -S python-pip
```

Installing package using pip
```
pip3 install pymewc
```

## How to use the package

To check whether the python package is working and responding perfectly

```sh
import pymewc
pymewc.hello()
```

For printing what the serial monitor prints:

```sh
import pymewc
pymewc.serial() # It asks for 2 parameters
# 1- The com-port('com4' or /dev/ttyACMO) depending on the os windows and *ux respectively
# 2- The baud rate
```

 **Adding few other features which are digitalRead and digitalWrite functionalites(In development will be live soon)**


## Development

Want to contribute? Great!

I will always welcome everyone contributers to contribute to the project which will be live soon. Hope it hits the market hard

## Screenshot of the outputs

![The Scope Image](https://github.com/gr8rithic/Pymewc/blob/master/realtime_scope.png)

**The scope image output in the matplotlib output window (Scoping Image output)**


## License

MIT

**Free Software, Hell Yeah!**
