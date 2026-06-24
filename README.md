# Pymewc ( Python Microcontroller Interface)

## _Making your microcontroller connect with python_

_version: 0.2.0 Beta_

[![PyPI](https://img.shields.io/pypi/v/pymewc)](https://pypi.org/project/pymewc/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pymewc)](https://pypi.org/project/pymewc/)
[![PyPI - License](https://img.shields.io/pypi/l/pymewc)](https://github.com/gr8rithic/Pymewc/blob/master/LICENSE)
[![PyPI downloads](https://img.shields.io/pypi/dm/pymewc.svg?style=flat)](https://pypi.org/project/pymewc/)
[![Contributions](https://img.shields.io/badge/contributions-welcome-green.svg)](https://github.com/gr8rithic/Pymewc)

- Pymewc is a new and innovative python library that can be used for connecting python with the microcontroller world.
- Pymewc is a lightweight package that aims for simplicity yet performs complex tasks with ease.

## Features

- Read data from each pin of the microcontroller
- Read data printed on the serial monitor window
- Scope any analog pin (default A0) at up to 100 Hz
- Blink and control digital pins
- List the available serial ports for quick connection
- Writing programs to the microcontroller (development stage)
- Sending data to the local cloud service / running an Apache server (development stage)

## Installation

Pymewc requires [Python](https://www.python.org/) v3.6+ to run, but is extensively tested and recommends using Python version > 3.7

Install the dependencies and packages and thats it.

### For windows

```sh
pip install pymewc
```

#### For linux and unix based Operating systems


**Downloading pip on linux based operating systems**

Debian and Debian Based distros(Ubuntu, Mint etc)

```sh
sudo apt install python3-pip
```

For Arch and Arch Based distros(Manjaro, Endevour etc)

```sh
sudo  pacman -S python-pip
```

Installing package using pip

```sh
pip3 install pymewc
```

## How to use the package

Import the package once and call the function you need. Every connection
function accepts arguments (so you can script it) or prompts you when called
without arguments.

**Check that the package is installed correctly**

```python
import pymewc
pymewc.hello()
```

**Show author and project information**

```python
import pymewc
pymewc.about()
```

**List the available serial ports**

```python
import pymewc
pymewc.list_ports()   # e.g. ['COM4'] or ['/dev/ttyACM0']
```

**Blink an LED on a digital pin**

```python
import pymewc
pymewc.blink()                                              # interactive prompts
pymewc.blink(pin=13, delay_sec=0.5, com_port="COM4", count=10)
```

**Print what the serial monitor prints**

```python
import pymewc
pymewc.serial()                                            # runs until Ctrl+C
pymewc.serial(com_port="COM4", baud_rate=9600)
```

**Print a fixed number of lines from the serial monitor**

```python
import pymewc
pymewc.serial_discrete()                                   # asks how many lines
pymewc.serial_discrete(count=20, com_port="COM4", baud_rate=9600)
```

**Scope an analog pin in real time**

```python
import pymewc
pymewc.scope()                                             # defaults to A0
pymewc.scope(com_port="COM4", analog_pin=1, sampling_rate=100)
```

**Set a digital pin HIGH or LOW**

```python
import pymewc
pymewc.digital_write()                                     # interactive prompts
pymewc.digital_write(pin=13, value=1, com_port="COM4")
```


## Roadmap

- Digital read helper for microcontrollers (`digital_write` is available)
- Multiple scopes running at the same time
- Writing programs to the microcontroller from Python

## Running the tests

The hardware-independent tests use only the Python standard library:

```sh
python -m unittest discover
```

## Want to help??

Want to contribute? Great!

I will always welcome everyone who wants to contribute to the project. Hope it hits the market hard.

## Screenshot of the outputs

![The Scope Image](https://github.com/gr8rithic/Pymewc/blob/master/realtime_scope.png)

**The scope image output in the matplotlib output window (Scoping Image output)**


## License

MIT

**Free Software, Hell Yeah!**

