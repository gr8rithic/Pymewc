import os
import re

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(HERE, *parts), encoding="utf-8") as handle:
        return handle.read()


def find_version(*parts):
    version_file = read(*parts)
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', version_file, re.M)
    if not match:
        raise RuntimeError("Unable to find __version__ string.")
    return match.group(1)


LONG_DESCRIPTION = read("README.md")
VERSION = find_version("pymewc", "__init__.py")
DESCRIPTION = "Microcontroller and Python interface"

setup(
    name="pymewc",
    version=VERSION,
    author="Rithic C H",
    author_email="gr8rithic@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/gr8rithic/Pymewc",
    project_urls={
        "Source": "https://github.com/gr8rithic/Pymewc",
        "Bug Tracker": "https://github.com/gr8rithic/Pymewc/issues",
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.6",
    install_requires=["pyserial", "pyfirmata2", "matplotlib", "numpy"],
    keywords=["python", "IoT", "microcontroller", "Arduino", "serial"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
)
