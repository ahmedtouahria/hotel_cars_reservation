from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def activitys(request):
    if 'aark' in request.GET:
        name=request.GET['name']
        mark=request.GET['mark']
        activitys=Activity.objects.filter(Q(type_activity__icontains=name) & Q(mark__icontains=mark) )
    else:
        activitys=Activity.objects.all()
    context={
        "activitys":activitys
        
    }
    return render(request,"activity/pages/activity.html",context)
def activity(request,pk):
    try:
        activity=Activity.objects.get(id=pk)
    except Activity.DoesNotExist:
        activity=None   
    if request.method=="POST":
        start_date=request.POST["start_date"]
        final_date=request.POST["final_date"]
        if request.user.is_authenticated:
            reserve=ReservationActivity(client=request.user,activity=activity,Date_debut=start_date,Date_fin=final_date)
            reserve.save()
            facture=FactureActivity(reservation=reserve,montant=activity.prix)
            facture.save()
            
        else:
            username=request.POST['f_name']+request.POST['l_name']
            email=request.POST['email']
            client=User(username=username,email=email,password="12345678")
            client.save() 
            reserve=ReservationActivity(client=client,activity=activity,Date_debut=start_date,Date_fin=final_date)
            reserve.save()
            facture=FactureActivity(reservation=reserve,montant=activity.prix)
            facture.save()
        messages.add_message(request, messages.INFO, 'Booking Activity successfully ! ')
    context={
        "activity":activity,
    }
    return render(request,"activity/pages/reservation.html",context)