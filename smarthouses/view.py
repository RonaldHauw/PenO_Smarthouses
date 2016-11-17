
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import smarthouses







def index(request):

    #return HttpResponse("Welcome to the demo.")

    template = loader.get_template('smarthouses')
    return HttpResponse(template.render(request))







