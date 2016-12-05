from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import House,Room
from helpfunctions import *
from Communicatie import *
import time
import timeit
from neighbourhood.models import Smart_Devices

# def change_statusold(request, appliance_id, param_to_change, value):
#     """
#     verandert de opgegeven parameter van een  apparaat in de gegeven value
#     en stuurt dit door via informatie
#     """
#     app = Smart_Devices.objects.get(id=appliance_id)
#     room = app.room
#     house = room.house
#     message = {'%d0%s0%s' % (room.shortcut, param_to_change, value) # dit vult de placeholders in
#     SendInformation('%s:8080' % house.ip, message) # eerst de standaard url die naar het huis verwijst, in die huis bevat de message
#     # de room waarnaar het moet gaan

def change_status(request, house_ip, room_id, device_ref_id, value):
    """
    verandert de opgegeven parameter van een  apparaat in de gegeven value
    en stuurt dit door via informatie
    """

    message = make_huge_string('change_status',room_id,device_ref_id,'status',value,'input','0')
    SendInformation('%s:8080' % house_ip, message) # eerst de standaard url die naar het huis verwijst, in die huis bevat de message
    # de room waarnaar het moet gaan




# def ledaan(request):
#     SendInformation('169.254.173.25:8080','LV01100')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))
#
# def leduit(request):
#     SendInformation('169.254.173.25:8080', 'LV01000')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))
#
# def led2aan(request):
#     SendInformation('169.254.173.25:8080','LV02100')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))
#
# def led2uit(request):
#     SendInformation('169.254.173.25:8080', 'LV02000')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))
#
#
# def led2fel(request):
#     SendInformation('169.254.173.25:8080','LV02060')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))
#
# def led2zwak(request):
#     SendInformation('169.254.173.25:8080', 'LV02030')
#     template = loader.get_template('testinterface.html')
#     return HttpResponse(template.render(request))

def update_clock(curtime):
    hour,minute = maketim()
    html ="""
    <html>
    <
    """

tijd_hele_dag = 240
def centralcontrol(request):
    """
    het programma dat de central control managet
    """

    ### continue loop die per stap kijkt naar de tijd, de inputs en dan de database en commando's bijhorden uitvoerd
    starttime=timeit.default_timer()

    #### klaarzetten: status van alle apparaten is uit en initialiseren
    turnalloff()




    while timeit.default_timer() - starttime < tijd_hele_dag:
        ###########
        ###
        ### naar de database kijken en zien welke apparaten er aan staan op dit moment of niet
        ### indien een apparaat volgens de database op dit tijdstip een andere waarde moet hebben
        ### stuurt deze een boodschap naar het betrokken apparaat. Tegelijk
        ###
        ############


        curtime=timeit.default_timer()
        update_clock(curtime)

        price = getprice(curtime)
        solar = getsolar(curtime)
        wind = getwind(curtime)



        neig = House.objects.all()

        for house in neig: #### itereren over alle apparaten ###
            for room in house.room_set.all():
                 ## in de database bij elk te optimaliseren device nog een attribuut geplande tijd? en huidige status##
                for smart_device in room.smart_devices_set.all():
                    curplan = getcurplan(smart_device,curtime) ## geeft de status dat het apparaat zou moeten hebben terug
                    curstatus = smart_device.status
                    cur_id = smart_device.ref_id

                    if curplan != curstatus:
                        change_status(request,cur_id,curplan) ### doorsturen naar huisjes
                        smart_device.status = curplan


                for fridge in room.fridges_set.all():
                    curplan = getcurplan(fridge, curtime)  ## geeft de status dat het apparaat zou moeten hebben terug
                    curstatus = fridge.status
                    cur_id = fridge.ref_id

                    if curplan != curstatus:
                        change_status(request, cur_id, curplan)  ### doorsturen naar huisjes
                        fridge.status = curplan

                for battery in room.battery_set.all():
                    curplan = getcurplan(battery,
                                         curtime)  ## geeft de status dat het apparaat zou moeten hebben terug
                    curstatus = battery.status
                    cur_id = battery.ref_id

                    if curplan != curstatus:
                        change_status(request, cur_id, curplan)  ### doorsturen naar huisjes
                        battery.status = curplan

                for heater in room.heating_set.all():
                    curplan = getcurplan(heater,
                                         curtime)  ## geeft de status dat het apparaat zou moeten hebben terug
                    curstatus = heater.status
                    cur_id = heater.ref_id

                    if curplan != curstatus:
                        change_status(request, cur_id, curplan)  ### doorsturen naar huisjes
                        heater.status = curplan

                for dumb_device in room.stupid_devices_set.all():
                    curplan = getcurplan(dumb_device,
                                         curtime)  ## geeft de status dat het apparaat zou moeten hebben terug
                    curstatus = dumb_device.status
                    cur_id = dumb_device.ref_id

                    if curplan != curstatus:
                        change_status(request, cur_id, curplan)  ### doorsturen naar huisjes
                        dumb_device.status = curplan






        #### !!!!!! als een lamp momenteel aangepast moet worden moet dit in de database worden gedaan !!!!! #####
        #### !!!!!! Dit programma gaat gewoon kijken naar het resultaat van de optimalistatie en in functie van de tijd
        ###         De status van de betrokken apparaten aanpassen



def time_tijd_hele_dag_naar_24(curtime):
    fractie = curtime / tijd_hele_dag
    return math.floor(fractie*24)

def time_tijd_hele_dag_naar_96(curtime):
    fractie =curtime/tijd_hele_dag
    return math.floor(fractie*96)

def print_time(curtime):


    return time_tijd_hele_dag_naar_24(curtime)





def give_time_given_96(number):
    """
    Deze functie geeft een waarde weer van 1 tem 96 dat overeenstemt met de tijd op een bepaalde dag.
    Elk getal staat gelijgik aan een kwartier. vb 26 is het 26e kwartier van de dag
    :param time: vb '15:46'
    :return:
    """

    hour = int(number/4)
    minute = (number%4)*15

    return str(hour) + ':' + str(minute)



