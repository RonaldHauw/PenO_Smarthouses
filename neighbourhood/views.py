from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room

def index(request):

    #return HttpResponse("Welcome to the neighbourhood.")

    template = loader.get_template('neighbourhood/index.html')
    return HttpResponse(template.render(request))

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


def test(request):
    template = loader.get_template('neighbourhood/test.html')
    return HttpResponse(template.render(request))

def Demo_homepage(request):
    template = loader.get_template('neighbourhood/demo_homepage.html')
    return HttpResponse(template.render(request))

def contact(request):
    template = loader.get_template('neighbourhood/contact_page.html')
    return HttpResponse(template.render(request))

def demo_uitleg(request):
    template = loader.get_template('neighbourhood/Demo_uitleg.html')
    return HttpResponse(template.render(request))