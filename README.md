# IddSampleDriverGUI
GUI for modifying options.txt from https://github.com/ge9/IddSampleDriver

![alt text](https://github.com/s-liwka/IddSampleDriverGUI/blob/main/img/screenshot1.png?raw=true)

## Installation

(I wanted to make a binary but pyinstaller refuses to work)

1. Download IddSampleDriver if you haven't already

2. Install Python (Im using 3.11.4) and select ADD TO PATH

https://www.python.org/downloads/

3. Clone the repo
```
git clone https://github.com/s-liwka/IddSampleDriverGUI
```
4. (OPTIONAL) Make a venv
```
python -m IddSampleDriverGUI-venv
```
5. (OPTIONAL) Activate the venv
```
IddSampleDriverGUI-venv\Scripts\activate.bat
```
6. Install requirements
```
pip install -r requirements.txt
```
7. Before you start the script, format your current option.txt to remove all comments, and (optionally) add one with your device id!!! The file should look like this:
```
<number of monitors>
#<Device ID>
width, height, refresh rate
width, height, refresh rate
...
```
7. Run the script as admin
```
python IddSampleDriverGUI.py
```
