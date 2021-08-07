from setuptools import setup, find_packages
import codecs
import os

with open("README.md", "r") as fh:
    LONG_DESCRIPTION= fh.read()

VERSION = '0.0.9.1'
DESCRIPTION = 'Microcontroller and python interface'

# Setting up
setup(
    name="pymewc",
    version=VERSION,
    author="Rithic C H",
    author_email="gr8rithic@gmail.com",
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pyserial', 'pyttsx3', 'setuptools', 'pyfirmata2', 'matplotlib', 'numpy'],
    keywords=['python', 'IoT', 'microcontroller', 'Arduino', 'Text-to-speech'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
