from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
from helpfunctions import *
import time


def functiontest(request):
    pass

def centralcontrol(request):
    """
    het programma dat de central control managet
    """

    ### continue loop die per stap kijkt naar de tijd, de inputs en dan de database en commando's bijhorden uitvoerd
    starttime=time.clock()

    #### klaarzetten: status van alle apparaten is uit
    turnalloff()
    curstatus = getstatus(starttime)


    while starttime - time.clock() < 100:
        ###########
        ###
        ### naar de database kijken en zien welke apparaten er aan staan op dit moment of niet
        ### indien een apparaat volgens de database op dit tijdstip een andere waarde moet hebben
        ### stuurt deze een boodschap naar het betrokken apparaat
        ###
        ############

        oldstatus = curstatus
        curtime=time.clock()
        curstatus = getstatus(curtime)


        for device in curstatus:
            if curstatus[device] != oldstatus[device]:
                succes = sendmessage(device,curstatus[device])
                if not succes:
                    displayalert('message not succeeded')
                else:

                    displayalert('status van ' + sayhello(device)+ "aangepast naar" + str(curstatus[device]))

        #### !!!!!! als een lamp momenteel aangepast moet worden moet dit in de database worden gedaan !!!!! #####
        #### !!!!!! Dit programma gaat gewoon kijken naar het resultaat van de optimalistatie en in functie van de tijd
        ###         De status van de betrokken apparaten aanpassen










