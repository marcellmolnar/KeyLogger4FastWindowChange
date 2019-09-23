# KeyLogger4FastWindowChange
Running this Python script will search for double space press and switch the current view to a specific window.

# Prerequisite:
Installed Python. (https://www.python.org/downloads/)

Installed pywin32 (after download: python -m pip install .whl) (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32)

Installed pynput. (python -m pip install pynput)



In the script change "windowToOpen" variable to the exact name of the window you want to change to. 

If you start the script and double press the space, the given window will be opened.

The maximal time difference between presses can be adjusted, but 200 ms will be fine.

Some window-name examples are in the script.

**IMPORTANT!**

The window must be opened and running in background (minimised!). The script cannot start the program.