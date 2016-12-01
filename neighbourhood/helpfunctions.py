from models import *
from auxilary import *

def commit_change(appliance_id=None, value=None):
    """
    verandert de opgegeven parameter van een  apparaat in de gegeven value
    en stuurt dit door via informatie
    """

    app = Smart_Devices.objects.get(id=appliance_id)
    room = app.room
    house = room.house
    pin = Smart_Devices.pin
    message = { 'function': commit_change,
                'room': room.shortcut,
                'unique_id': appliance_id,
                'param_to_change':'status',
                'new_value':value,
                'pin': pin}
    SendInformation('%s:8080' % house.ip, message) # eerst de standaard url die naar het huis verwijst, in die huis bevat de message
    # de room waarnaar het moet gaan




##### 1 pagina, huisje aansturen met extra uitleg, tijdsklok,





def turnalloff():
    """
    zet de status van alle apparaten uit en daarmee ook het verbruik terug op nul. In zowel de database als in de huisjes
    !!!!!! initialisatie van alle apparaten !!!!!
    """
    neigh = House.objects.all()

    ### itereren over alle apparaten ###
    for house in neigh:
        for room in house.room_set.all():
            for smart_device in room.smart_devices_set.all():
                if smart_device.status != 000:
                    curid = smart_device.ref_id
                    commit_change(curid,000) ### verandering doorsturen naar huis
                    smart_device.status = 000 ### verandering doorsturen naar database


            for fridge in room.fridges_set.all():
                if fridge.status != 000:
                    curid = fridge.ref_id
                    commit_change(curid,000) ### verandering doorsturen naar huis
                    fridge.status = 000 ### verandering doorsturen naar database

            for battery in room.battery_set.all():
                if battery.status != 000:
                    curid = battery.ref_id
                    commit_change(curid,000) ### verandering doorsturen naar huis
                    battery.status = 000 ### verandering doorsturen naar database
            for heater in room.heating_set.all():
                if heater.status != 000:
                    curid = heater.ref_id
                    commit_change(curid,000) ### verandering doorsturen naar huis
                    heater.status = 000 ### verandering doorsturen naar database
            for dumb_device in room.stupid_devices_set.all():
                if dumb_device.status != 000:
                    curid = dumb_device.ref_id
                    commit_change(curid,000) ### verandering doorsturen naar huis
                    dumb_device.status = 000 ### verandering doorsturen naar database










def getwind(house):
    pass



def getsolar(house):
    pass



def getprice(time):
    """
    vragen aan hanspeter (csv)
    """
    pass

def generate_code(house,room,type,id,status):
    pass

def getcurplan(device,time):
    """
    haalt uit de database de huidige planning (in procent) in functie van de tijd

    """

def getcuruse(device):
    """
    geeft de huidige stand van het apparaat terug
    """