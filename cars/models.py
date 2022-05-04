from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
# Car Table
class Car(models.Model):
    mark=models.CharField(max_length=120,null=True)
    phone_number = models.CharField(max_length=10,validators=[phone_regex],)
    type_car=models.CharField(max_length=12)
    prix = models.FloatField(default=0)
    puissance = models.CharField(max_length=120,null=True)
    image = models.ImageField(upload_to='media/car/')
    disponibilité = models.BooleanField(default=True)
    def __str__(self):
        return f'car N-{self.id}'
class ReservationCar(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reserve_car")
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="car")
    Date_debut = models.DateField(auto_now=False)
    Date_fin = models.DateField(auto_now=False)
    def __str__(self):
        return f'{self.client} - {self.car}'

class FactureCar(models.Model):
    reservation=models.OneToOneField(ReservationCar,on_delete=models.CASCADE)
    PAY_TYPE = (('cach', 'cach'), ('card', 'card'),)
    Date_facteur = models.DateField(auto_now=True)
    mode_payment=models.CharField(max_length=120,choices=PAY_TYPE,default="card")
    montant=models.FloatField(default=0)
    def __str__(self):
        return str(self.reservation) 

