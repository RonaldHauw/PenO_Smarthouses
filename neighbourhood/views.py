from django.http import HttpResponse
from django.template import loader
from models import *
from django.shortcuts import render

from django.template.response import TemplateResponse



def house(request,house_id):

    template = loader.get_template('neighbourhood/house.html')
    # context = {'house': House.objects.get(ip_address=house_id)}
    context = {'house': house_id}
    return TemplateResponse(request,template,context)

def room(request,id):

    all_rooms = Room.objects.all()
    context = {'room': Room.objects.get(id=id)}
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

def indexcentralcontrol(request):
    template = loader.get_template('indexcentralcontrol.html')
    return HttpResponse(template.render(request))

def testinterface(request):
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))


def handmatig(request):
    template = loader.get_template('Handmatig.html')
    return HttpResponse(template.render(request))