from django.forms import ModelForm
from django import forms
from .models import Flight,Passengers
from django.core.exceptions import ValidationError
class flight_form(forms.ModelForm):
    class Meta:
        model=Flight
        fields='__all__'
        
class passenger_form(forms.ModelForm):
    class Meta:
        model=Passengers
        fields=['first','last']
        
    # def clean_first(self):
    #     first=self.cleaned_data.get('first')
    #     last=self.cleaned_data.get('last')
    #     if first=="":
    #         raise forms.ValidationError('This field cannot be left blank')

    #     for instance in Passengers.object.all():
    #         if instance.first==first and instance.last==last:
    #             raise forms.ValidationError('This field already exists')


    

