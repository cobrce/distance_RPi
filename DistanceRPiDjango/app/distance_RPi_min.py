# based on https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
import os
import time
import RPi.GPIO as g

trigger = 21
echo = 16

global initialized
initialized = False

def init():
    g.setmode(g.BCM)
    g.setup(echo,g.IN)
    g.setup(trigger,g.OUT)
    global initialized
    initialized = True

def Trigger():
    g.output(trigger,True)
    time.sleep(0.00001)
    g.output(trigger,False)

def WaitForEdge(value):
    while g.input(echo) != value:
        pass

def measure():
    global initialized
    if not initialized:
        init()
        
    Trigger()

    WaitForEdge(1)
    startime = time.time()

    WaitForEdge(0)
    endtime = time.time()

    delta = endtime - startime
    distance = delta * 34300 / 2
    return distance