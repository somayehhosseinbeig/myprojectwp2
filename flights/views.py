from django.shortcuts import render
from .models import Flight,Passenger,Airport
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
    
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(), # type: ignore
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request,flight_id):
    if request.method == "POST":
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        flight = Flight.objects.get(pk=flight_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
   
    
