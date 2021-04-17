from django.db import models
from django import forms

# Create your models here.

class Airports(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code}: {self.city}"
    

class Flight(models.Model):
    origin=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="depatures")
    destination=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()  

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Passengers(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flight=models.ManyToManyField(Flight,blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last}"
    
    


    
