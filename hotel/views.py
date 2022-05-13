from django.shortcuts import render

from activity.models import Activity
from .models import *
from django.contrib import messages
from django.db.models import  Q
from cars.models import Car
# Create your views here.
def index(request):
    context={
        "rooms":Chambre.objects.all(),
        "cars":Car.objects.all(),
        "activitys":Activity.objects.all(),
        
    }
    return render(request,"hotel/pages/index.html",context)

def rooms(request):
    if 'address' in request.GET:
        try:
            type=request.GET['type']
        except:
            type=""    
        address=request.GET['address']
        hotel=Hotel.objects.filter(adress__icontains=address).first()
        rooms=Chambre.objects.filter(Q(type_chambre__icontains=type) & Q(nome_hotel=hotel) )
    else:
        rooms=Chambre.objects.all()
    context={
        "rooms":rooms
        
    }
    return render(request,"hotel/pages/rooms.html",context)

def reserve(request,pk):
    try:
        room=Chambre.objects.get(id=pk)
    except Chambre.DoesNotExist:
        room=None   
    if request.method=="POST":
        if request.user.is_authenticated:
            start_date=request.POST["start_date"]
            final_date=request.POST["final_date"]
            reserve=Reservation(client=request.user,chambre=room,Date_debut=start_date,Date_fin=final_date)
            reserve.save()
            facture=Facture(reservation=reserve)
            facture.save()
            
            messages.add_message(request, messages.INFO, 'Booking room successfully ! ')
    context={
        "room":room,
    }
    return render(request,"hotel/pages/reservations.html",context)