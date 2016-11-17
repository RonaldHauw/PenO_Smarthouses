from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room





def indexcentralcontrol(request):
    template = loader.get_template('indexcentralcontrol.html')
    return HttpResponse(template.render(request))

def testinterface(request):
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))


