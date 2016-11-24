from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
from helpfunctions import *
from Communicatie import *
import time


def ledaan(request):
    SendInformation('169.254.173.25:8080','LV01100')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))

def leduit(request):
    SendInformation('169.254.173.25:8080', 'LV01000')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))

def led2aan(request):
    SendInformation('169.254.173.25:8080','LV02100')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))

def led2uit(request):
    SendInformation('169.254.173.25:8080', 'LV02000')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))


def led2fel(request):
    SendInformation('169.254.173.25:8080','LV02060')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))

def led2zwak(request):
    SendInformation('169.254.173.25:8080', 'LV02030')
    template = loader.get_template('testinterface.html')
    return HttpResponse(template.render(request))




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
        price = getprice(company)



        for house in neighbourhood:
            solar = getsolar(house)
            wind  = getwind(house)

            for room in house:
                for device in room: ## in de database bij elk te optimaliseren device nog een attribuut geplande tijd? en huidige status##
                    plan = getcurplan(device,time)
                    if  plan != getcuruse(device): ## plan bevat op welke stand het apparaat moet aanstaan nu
                        succes = sendmessage(getcode(device),plan)
                        if not succes:
                            displayalert('message not succeeded')
                        else:
                            displayalert('status van ' + sayhello(device)+ "aangepast naar" + str(curstatus[device]))

        #### !!!!!! als een lamp momenteel aangepast moet worden moet dit in de database worden gedaan !!!!! #####
        #### !!!!!! Dit programma gaat gewoon kijken naar het resultaat van de optimalistatie en in functie van de tijd
        ###         De status van de betrokken apparaten aanpassen










