# python_project_license_checker
Check/list Python packages in your current project.

## About
Helps with reporting license issues by gathers license, version and requirements for all your installed packages in your current Python project.
Simple, lightweight, and fast.


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
