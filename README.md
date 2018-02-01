# Python Project License Checker
Check or lists Python package license for your current project.

Simple, lightweight, and fast.

## About
Helps with reporting any potential license issues by gathers license, version, & requirements, for all the installed packages in your current Python project.


## How to install
Add file to your projects root directory, if running a virtualenv make sure it is running. 

## How to use

```
# Prints out in terminal.
python check.py -t

# Writes csv file to current location.
python check.py -f

```

### Example output in terminal:
```
-----
Flask: BSD
License: http://github.com/pallets/flask/ Home-page: http://github.com/pallets/flask/
Requires: Werkzeug (>=0.7) | click (>=2.0) | itsdangerous (>=0.21)
-----
```
