# based on https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
import os
import time
import RPi.GPIO as g
from guizero import App, Text,Slider

trigger = 21
echo = 16

def init():
    g.setmode(g.BCM)
    g.setup(echo,g.IN)
    g.setup(trigger,g.OUT)

def Trigger():
    g.output(trigger,True)
    time.sleep(0.00001)
    g.output(trigger,False)

def WaitForEdge(value):
    while g.input(echo) != value:
        pass

def RepeatMeasure(time):
    txt.cancel(measure)
    txt.repeat(time,measure)
    
def GUI():
    app = App(title = "Distance",width = 230,height= 70,layout="grid")
    
    Text(app,text = "Rate (ms) :",grid=[0,0],align = "left")
    slider = Slider(app,command=RepeatMeasure,start = 50,end = 2000,grid = [1,0],align = "left")
    slider.value = "100"
    
    
    Text(app,text = "Distance (cm) : ", grid = [0,1],align="left")    
    global txt
    txt = Text(app,text="Dist",grid = [1,1],align="left")
    RepeatMeasure(100)
    
    app.display()
        
    
def Display(distance):
    #print(distance)
    txt.value = "%0.2f" % distance
    
def measure():
    
    Trigger()

    WaitForEdge(1)
    startime = time.time()

    WaitForEdge(0)
    endtime = time.time()

    delta = endtime - startime
    distance = delta * 34300 / 2
    Display(distance)
    
def main():
    init()
    GUI()
	
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        g.cleanup()