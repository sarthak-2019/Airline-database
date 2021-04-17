from django.contrib import admin


from flights.models import Flight,Airports,Passengers
# Register your models here.

admin.site.register(Flight)
admin.site.register(Airports)
admin.site.register(Passengers)