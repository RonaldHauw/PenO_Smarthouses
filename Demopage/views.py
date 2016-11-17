from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
import Demopage



def Demo_homepage(request):
    template = loader.get_template('demo/demo_homepage.html')
    return HttpResponse(template.render(request))

def contact(request):
    template = loader.get_template('demo/contact_page.html')
    return HttpResponse(template.render(request))

def demo_uitleg(request):
    template = loader.get_template('demo/Demo_uitleg.html')
    return HttpResponse(template.render(request))

