from django.urls import path

from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:flightid>",views.flight,name="flight"),
    path("<int:flightid>/book",views.book,name="book"),
    path("<int:flightid>/deletep_database",views.delete_passenger_database,name="deletep_database"),
    path("addflight",views.add_flight,name="addflight"),
    path("<int:flightid>/addp",views.add_passenger,name="addp"),
    path("<int:flightid>/deletep",views.delete_passenger,name="deletep"),
    path("<int:flightid>/addp_database",views.add_passenger_database,name="addp_database")
]
