"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
from subprocess import Popen,PIPE,STDOUT
from random import randint
import time
import os
import sys
import json
from django.http import Http404
import signal

p = None
distance = 0
running = True

def ExitHandler(*args):
    from threading import get_ident
    
    global p
    if p != None:
        p.kill()
        print("(%X) Reader process killed" % get_ident())
    else:
        print("(%x) Reader process not running" % get_ident())
    print("(%x) Server shutdown" % get_ident())
    sys.exit(0)

def Measure():
    global distance
    global running
    
    if running:
        dist = float(p.stdout.readline())
        #print(dist)
        if dist > 250:
            distance = "Too far"
        elif dist < 2:
            distance = "Too near"
        else:
            distance = "%0.2f" % dist
    return distance
    
def CheckMethod(method):
    if method == "GET":
        raise Http404("Url not existing")
    
def resumesuspend(request):
    global running
    
    CheckMethod(request.method)
    
    if request.user.is_authenticated and 'stop' in request.POST :
        try:
            running = not bool(int(request.POST['stop']))
        except:
            pass
    return HttpResponse("")

def read(request):
    global running
    
    CheckMethod(request.method)
    CheckReader()
    
    if running:
        status = "Running"
    else:
        status = "Suspended"
    return HttpResponse(json.dumps({"dist" : "Distance (cm) :  {}".format(Measure()),"status" : status}))

def CheckReader():
    global p
    if p == None:
        p = Popen(["python3","app/distance_RPi_min.py"],stdin=PIPE,stdout=PIPE,stderr=STDOUT)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    
    CheckReader()
    return render(request,
        'app/index.html',
        {
            'title':'Ultrasonic sensor distance measure',
            'year':datetime.now().year,
            'distance' : 300,
        })

def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render_to_response(your_custom_template, ctx)