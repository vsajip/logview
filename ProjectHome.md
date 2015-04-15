# Overview #
This project provides a viewer for logging output produced by Python programs using its standard library's logging package and sending logging events to TCP, UDP and ZeroMQ PUB sockets.

Screenshot:

![http://i.imgur.com/5DPno.png](http://i.imgur.com/5DPno.png)

# Installation #

This application has dependencies on `Qt4`/`PyQt4` (required) and `ZeroMQ`/`pyzmq` (optional). None of the dependencies are easily installable, so a source distribution is provided (for use where you have `Qt4` and `PyQt4`, and optionally `ZeroMQ` and `pyzmq`, already installed), and a set of binary distributions which contain all required dependencies is provided for those who either don't have `Qt`/`PyQt` or have an old version which doesn't work with this application (Note: this application has been tested with `Qt` 4.7 and later with `PyQt` 4.7.4 and later).

## Source distribution ##

Note that a `setup.py` is not included. Just unarchive into a folder and run `logview.py`. It's assumed that `PyQt4` and (optionally) `pyzmq` will be found on the Python module search path.

## Linux binary distribution ##

This was built on a Ubuntu Hardy machine and should work on most recent Linux distributions. Smoke tests were carried out on: Fedora 14, Ubuntu (Jaunty, Karmic, Maverick), Debian Lenny, Linux Mint 10 (Ubuntu and Debian variants) and OpenSUSE 11.3. On all these, the distribution seems to work.

To use, unarchive and run the `logview` executable.

## Windows binary distribution ##

This was built on a Windows 7 machine and smoke-tested on Windows 7 and Windows XP with success.

To use, unarchive and run the `logview.exe` executable.

## Mac OS X binary distribution ##

This was built and smoke-tested on a Leopard machine with Python 2.5.

To use, mount the DMG normally, and to install on your system, drag the `LogView` icon and drop it on the Applications icon. This installs the `LogView` package on your system (in the Applications folder), and you can then unmount and discard the DMG. To run, double-click on the `LogView` icon.

# Usage #

On all platforms, invoking with `--help` prints the details of available command-line options.

By default, the system listens on TCP at 0.0.0.0:9020, UDP on 0.0.0.0:9021 and via a ZeroMQ SUB socket connected to tcp://localhost:9024. If you override with command line options, these are saved and used on subsequent runs.

The screenshot shows the appearance of the application. The panes can be resized using the splitters. Clicking on a node in the tree shows only the messages for that part of the hierarchy, and clicking on the Root logger node shows all messages. You can filter messages according to specific levels (not a threshold - e.g. you can see CRITICAL messages but filter out all others).

Collection of messages from the network happens automatically on starting and continues until the program is closed. If you scroll right to the bottom of the records pane when collecting, this is "sticky" and will cause the pane to scroll as collection proceeds, so that the last collected records remain in view. The automatic scrolling stops when you scroll off the bottom of the pane.

Clicking on a single record will display its details in the lower property-style pane, in order of decreasing interest. Values that contain newlines (such as exception text) will result in a `...` appearing in the rightmost column, clicking on which will display the multi-line text in a dialog box.

You can resize columns and reorder them using drag-and-drop. The "Columns..." button allows you to specify which columns are displayed, and their ordering.