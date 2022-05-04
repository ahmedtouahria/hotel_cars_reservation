from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def cars(request):
    if 'mark' in request.GET:
        name=request.GET['name']
        mark=request.GET['mark']
        cars=Car.objects.filter(Q(type_car__icontains=name) & Q(mark__icontains=mark) )
    else:
        cars=Car.objects.all()
    context={
        "cars":cars
        
    }
    return render(request,"car/pages/cars.html",context)
def car(request,pk):
    try:
        car=Car.objects.get(id=pk)
    except Car.DoesNotExist:
        car=None   
    if request.method=="POST":
        start_date=request.POST["start_date"]
        final_date=request.POST["final_date"]
        if request.user.is_authenticated:
            reserve=ReservationCar(client=request.user,car=car,Date_debut=start_date,Date_fin=final_date)
            reserve.save()
            facture=FactureCar(reservation=reserve,montant=car.prix)
            facture.save()
            
        else:
            username=request.POST['f_name']+request.POST['l_name']
            email=request.POST['email']
            client=User(username=username,email=email,password="12345678")    
            reserve=ReservationCar(client=client,car=car,Date_debut=start_date,Date_fin=final_date)
            reserve.save()
            facture=FactureCar(reservation=reserve,montant=car.prix)
            facture.save()
        messages.add_message(request, messages.INFO, 'Booking car successfully ! ')
    context={
        "car":car,
    }
    return render(request,"car/pages/reservation.html",context)