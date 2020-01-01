# Make a GUI in Python to automate 3 most done tasks
## Google Code-In 2019 Task made by [Alisha Mohanty](https://github.com/alishamohanty) and [Rahul Otwani](https://github.com/rahulotwani)

## Used dependencies
- [requests](https://requests.readthedocs.io/en/master/) for openweathermap fetching

## Usage
- Install dependencies `pip install -r requirements`
- Run `python src/main.py`

## How can I add this into autostart?
### On Windows
- Let' s create a **.bat** file inside `shell:startup` directory (e.g `automator.bat`)
- Put following content inside this file:
```bat
@echo off
python <absolute path to src/main.py file>
```

### On GNU/Linux
- Create a **.desktop** file inside `/etc/xdg/autostart`
- Put the following content into this file:
```ini
[Desktop Entry]
Type=Application
Name=Automator
Exec=python <absolute path to src/main.py file>
X-GNOME-Autostart-enabled=true
```
## How can I change my location for weather forecast?
Change `CITYNAME` constance inside `src/main.py`

### Made by Emilian **synnek1337** Zawrotny