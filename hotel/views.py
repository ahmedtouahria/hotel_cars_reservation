from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "rooms":Chambre.objects.all()
    }
    return render(request,"hotel/pages/index.html",context)

def rooms(request):
    context={
        "rooms":Chambre.objects.all()
        
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