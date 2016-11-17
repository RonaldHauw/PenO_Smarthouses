from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import TestBalkjes

def functiontest(request):
    """
    eerste testfase --> geef een warning

    """
    TestBalkjes.volume +=10


