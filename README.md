# distance_RPi
A Python project to use Raspberry PI 3 + HC-SR04 (ultrasonic sensor) to measure distance (based on [this](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/) tutorial)

![alt text](https://raw.githubusercontent.com/cobrce/distance_RPi/master/screenshot.png)

### Needed packages
* guizero
* RPi.GPIO

### Setup
* Wire the trigger and echo pins of the sensor to pin 21 and 16 (Broadcom) resp. of the RPi3
* Connect sensor Vcc to +5 and Gnd to 0

### Use
* Run the script
* Move the slider to change the refresh rate (default is 100ms)

# Web app
This is a Django web app to display the measured distance in web page instead of console/gui.
The app was developped in VisualStudio Community edition and so the templates are just modifications to the original ones.

![alt text](https://raw.githubusercontent.com/cobrce/distance_RPi/master/web-screenshot.png)

### Neede packages
* Django==1.11.13

### Setup
I'm using a virtual environment for the app and followed these steps:
```
git clone https://github.com/cobrce/distance_RPi.git
cd distance_RPi/DistanceRPiDjango
mkdir venv
python3 -m venv venv
source venv/bin/activate
pip3 install Django==1.11.13
python3 manage.py makemigrations
python3 manage.py migrate
pytohn3 manage.py createsuperuse
```
at this point you will be asked to create a super user (provide name, email and password of your choice)

### Use
if you don't see "(venv)" before the bash prompt use the following line (we suppose your current directory is distance_RPi/DistanceRPiDjango)
```
source venv/bin/activate
```
To run the server
```
python3 manage.py runserver YOUR_LOCAL_IP:PORT
```
Open a browser and navigate to YOUR_LOCAL_IP:PORT

### Login
by login with the super use you see a new button that allows you to Suspend/Resume the process
