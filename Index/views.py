from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
import Demopage



def Demo_homepage(request):
    template = loader.get_template('demo/demo_homepage.html')
    return HttpResponse(template.render(request))
