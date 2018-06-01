"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
from threading import Thread
from random import randint
import time
import os
import sys

### super user = { login : admin, password : admin258 }
if os.name == "nt":
    """ because in windows GPIO doesn't work."""
    def measure():
        return randint(0,300)
else:
    from app.distance_RPi_min import measure

th = None
distance = 0
running = True

def Measure():
    global distance
    global running

    while True:    
        if running:
            dist = measure()
            if dist > 250:
                distance = "Too far"
            elif dist < 2:
                distance = "Too near"
            else:
                distance = "%0.2f" % dist
            time.sleep(0.1)

def home(request):
    global th
    global distance
    global running

    """Renders the home page."""
    assert isinstance(request, HttpRequest)  
    
    if th == None:
        th = Thread(target = Measure)
        th.start()
    
    if request.user.is_authenticated:
        if 'stop' in request.POST :
            try:
                running =not bool(int(request.POST['stop']))
            except:
                pass

    if 'read' in request.POST:
        return HttpResponse("Distance (cm) :  {}".format(distance))
    else:
        return render(request,
            'app/index.html',
            {
                'title':'Ultrasonic sensor distance measure',
                'year':datetime.now().year,
                'distance' : 300,
            })
 