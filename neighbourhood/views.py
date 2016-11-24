# from neighbourhood import *
# from index import *
# from Demopage import *

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room

from django.template.response import TemplateResponse

def house(request,house_id):

    template = loader.get_template('neighbourhood/house.html')
    context = {
        'house': House.objects.get(id=house_id)
    }
    return TemplateResponse(request,template,context)

def room(request,id):

    all_rooms = Room.objects.all()
    context = {
        'room': Room.objects.get(id=id)
    }
    template = loader.get_template('neighbourhood/room.html')
   # return HttpResponse(template.render(context,request))
    return TemplateResponse(request,template,context)



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



def Root(request):
    template = loader.get_template('Index.html')
    return HttpResponse(template.render(request))

def centralcontrol(request):
    template = loader.get_template('indexcentralcontrol.html')
    return HttpResponse(template.render(request))

def Demo_homepage(request):
    template = loader.get_template('demo/demo_homepage.html')
    return HttpResponse(template.render(request))