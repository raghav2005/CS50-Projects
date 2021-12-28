# CONVERTERS


## CONTENTS

- [Video Demo](#video-demo)
- [Description](#description)
	- [Overview](#overview)
	- [main.py explanation](#main.py)
	- [requirements.txt explanation](#requirements.txt)
	- [APIs.py explanation](#apis.py)
	- [fonts folder explanation](#font-folder)
	- [images folder explanation](#images-folder)
	- [themes/button_themes.json explanation](#themes/button_themes.json)
	- [themes/dropdown_menu_themes.json explanation](#themes/dropdown_menu_themes.json)
- [Requirements](#requirements)
	- [Installing dependencies + running application](#python-libs-on-terminal)
	- [Getting the API + including it so it works](#python-file-for-api)


## VIDEO DEMO

### URL: https://youtu.be/xZ_ZtGUKh_g

## DESCRIPTION

### OVERVIEW
This is a program that was created using python, and it is intended to be
used to convert between some everyday and commonly used units. You can
click on the various buttons to take you to the different types of
measurements to convert between, and click the "M" or "P" button on your
keyboard to return to the main menu, or the previous screen you were on.
Most of the details on how to use the program are listed when you click on
the instructions button after opening the program, but before that, be sure
to scroll to the bottom of this README page or click [here](#python-file-for-api)
and follow the instructions to create an API and add that into a python file.

### MAIN.PY
This file contains the main python code that imports pygame, pygame_gui, 
the [APIs.py](#apis.py) file with the API, and ties together everything
in order to display the application and includes all the functionality and
conversions.

### REQUIREMENTS.TXT
This file contains all the requirements that need to be installed using pip.
For instructions on how to use this file to install the necessary dependencies,
click [here](#requirements).

### APIS.PY
This file has to be created by the user - instructions can be found by clicking
[here](#python-file-for-api).

### FONTS FOLDER
This folder contains the various fonts used in the application which are used
to display text in [main.py](#main.py).

### IMAGES FOLDER
This contains the png file which is used as the icon displayed in the dock,
instead of the regular pygame icon.

### THEMES/BUTTON_THEMES.JSON
This file contains the json code used to style the buttons in the application.

### THEMES/DROPDOWN_MENU_THEMES.JSON
This file contains the json code used to style the dropdown options and buttons
displayed in each of the different unit conversion pages.

## REQUIREMENTS

### PYTHON LIBS ON TERMINAL

Dependencies are in `requirements.txt`

1. To install the dependencies, first go to converters directory, once in,

- ON MAC run:
```
$ pip3 install -r requirements.txt
```
- ON WINDOWS run:
```
$ pip install -r requirements.txt
```

2. Afterwards, you can run the python file `main.py` with,

- ON MAC:
```
$ python3 main.py
```
* or
```
$ python main.py
```
depending on whatever python 3 is called on Terminal

- ON WINDOWS:
```
$ python main.py
```

### PYTHON FILE FOR API

In order to use the conversion API, you must first create a file called with
the filename `APIs.py`.

Once you have done this, visit https://fixer.io/ and sign up with a free plan,
following the instructions to get the API.

Once you have the api, open `APIs.py` and enter the following code, with 
YOURAPI replaced with the actual API as a string:

```python
fixer_API = YOURAPI

```

e.g.

```python
fixer_API = 'blahblahblahblahblahblahblahblahblah'

```
