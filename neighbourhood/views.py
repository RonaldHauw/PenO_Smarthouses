from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
from Demopage import *
from Index import *
from neighbourhood import *


def house(request,id):

    template = loader.get_template('neighbourhood/house.html')
    context = {
        'house': House.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def room(request,id):

    context = {
        'room': Room.objects.get(id=id)
    }
    template = loader.get_template('neighbourhood/room.html')
    return HttpResponse(template.render(context,request))



def indexneighbourhood(request):
    template = loader.get_template('neighbourhood/indexneighbourhood.html')
    return HttpResponse(template.render(request))

def Root(request):
    template = loader.get_template('Index.html')
    return HttpResponse(template.render(request))

def centralcontrol(request):
    template = loader.get_template('indexcentralcontrol.html')
    return HttpResponse(template.render(request))

def Demo_homepage(request):
    template = loader.get_template('demo/demo_homepage.html')
    return HttpResponse(template.render(request))



