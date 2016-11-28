from __future__ import unicode_literals
from django.db import models

from django.db import models

class Neighbourhood(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class House(models.Model):

    name = models.CharField(max_length=32)

    neighbourhood = models.ForeignKey(Neighbourhood)

    ip = models.CharField(max_length=32) # 169.254.173.25

    def __str__(self):
        return self.name


class Room(models.Model):

    #roomtypes = ((Kitchen,'Kitchen'),(Living_Room,'Living_Room'),(Hallway,'Hallway'),(Toilet,'Toilet'),(Laundry_Room,'Laundry_Room'),(Bedroom_1,'Bedroom_1'),(Bedroom_2,'Bedroom_2'),(Bathroom,'Bathroom'))

    house = models.ForeignKey(House)

    name = models.CharField(max_length=100)
    #smart_devices = models.CharField(max_length=100, default=' ')
    #EED = models.CharField(max_length=100, default=' ')
    #ENED = models.CharField(max_length=100, default=' ')

    description = models.TextField()

    def __str__(self):
        return self.name + '-' + self.house.name

####################################################################################################
####################################################################################################
##                                                                                                ##
##                                          ROOM TYPES                                            ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################
#
# energy efficient devices = EED
# energy non efficient devices = ENED


####################################################################################################
####################################################################################################
class Smart_Devices(models.Model):

    name = models.CharField(max_length=100)
    #id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    duration = models.CharField(max_length=100, default=0)
    deadline = models.CharField(max_length=100, default=0)

    description = models.TextField()
    room = models.ForeignKey(Room)


    def __str__(self):
        return self.name + '-' + self.room.name

    def getStatus(self, timestamp):
        self.tijdreeks# in django functionaliteit opzoeken


####################################################################################################
####################################################################################################
##                                                                                                ##
##                                        Smart Devices                                           ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################

class Boiler(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)

class Solar_BoIler(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)

class Electric_Car(Smart_Devices):

    percentage_battery = models.CharField(max_length=100, default=0)
    total_power = models.CharField(max_length=100, default=0)

class Washing_Machine(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)

class Dryer(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)

class Dishwasher(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)

class Fridge(Smart_Devices):

    temperature = models.CharField(max_length=100, default=0)


####################################################################################################
####################################################################################################

class Energy_Efficient_Devices(models.Model):


    name = models.CharField(max_length=100)
    #id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    duration = models.CharField(max_length=100, default=0)
    #amount = models.CharField(max_length=100, default=1)

    description = models.TextField()
    room = models.ForeignKey(Room)


    def __str__(self):
        return self.name + '-' + self.room.name

####################################################################################################
####################################################################################################
##                                                                                                ##
##                                  energy efficient devices                                      ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################


#class Lamps(Energy_Efficient_Devices):
#
#    pass
#
#class Television(Energy_Efficient_Devices):
#
#    pass
#
#class Coffee_Machine(Energy_Efficient_Devices):
#
#    pass
#
#class Oven(Energy_Efficient_Devices):
#
#    pass
#
#class Computer(Energy_Efficient_Devices):
#
#    pass
#
####################################################################################################
####################################################################################################

class Energy_Non_Efficient_Devices(models.Model):

    name = models.CharField(max_length=100)
    #id=models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    duration = models.CharField(max_length=100, default=0)
    #amount = models.CharField(max_length=100, default=1)

    description = models.TextField()
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name

####################################################################################################
####################################################################################################
##                                                                                                ##
##                                  energy non efficient devices                                  ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################

#class Lamps(Energy_Non_Efficient_Devices):
#
#    pass
#
#class Television(Energy_Non_Efficient_Devices):
#
#   pass
#
#class Coffee_Machine(Energy_Non_Efficient_Devices):
#
#    pass
#
class oven(Energy_Non_Efficient_Devices):

    temperature = models.CharField(max_length=100, default=0)

#class Computer(Energy_Non_Efficient_Devices):
#
#    pass
#
####################################################################################################
####################################################################################################

####################################################################################################
####################################################################################################
##                                                                                                ##
##                                        energy storage                                          ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################

class Battery(models.Model):
    name = models.CharField(max_length=100)
    #id = models.CharField(max_length=100)
    used_power_battery = models.CharField(max_length=100, default=0)
    available_power_battery = models.CharField(max_length=100, default=0)

    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + room.name





#############################################################################
#############################################################################


class Sensors(models.Model):

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100,default=0)

    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name

####################################################################################################
####################################################################################################

class Energy_Sources(models.Model):

    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    duration = models.CharField(max_length=100, default=0)

    room_energy_sources = models.ForeignKey(Room)

    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.name


####################################################################################################
####################################################################################################
##                                                                                                ##
##                                        energy sources                                          ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################

class Solar_Pannels(Energy_Sources):

    amount = models.CharField(max_length=100, default=0)

class wind_turbine(Energy_Sources):

    speed_wind = models.CharField(max_length=100, default=0)

#class Power_Plant(Energy_Sources):
#
#    pass
#
####################################################################################################
####################################################################################################

####################################################################################################
####################################################################################################
##                                                                                                ##
##                                          Total power                                           ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################
####################################################################################################

class Total_Power(models.Model):

    total_used_power = models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.total_used_power

class Weather(models.Model):

    wind_speed = models.CharField(max_length=100, default=0)
    temperature = models.CharField(max_length=100, default=0)
    light_intensity = models.CharField(max_length=100, default=0)

    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.wind_speed + '-' + self.temperature + '-' + self.light_intensity


class TestBalkjes(models.Model):
    volume = models.IntegerField()
    def __str__(self):
        return self.volume


