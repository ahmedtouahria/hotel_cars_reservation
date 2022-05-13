from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
# Hotel Table
class Hotel(models.Model):
    name = models.CharField(max_length=120)
    adress=models.CharField(max_length=120)
    code_postal=models.CharField(max_length=10)
    ville=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10,validators=[phone_regex],)
    def __str__(self) :
        return self.name
class Chambre(models.Model):
    VAR_TYPE = (('1', '1'), ('2', '2'), ('Family', 'Family'),)
    nome_hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14,validators=[phone_regex],)
    type_chambre=models.CharField(choices=VAR_TYPE,max_length=12)
    prix = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/pics')
    disponibilité = models.BooleanField(default=True)
    def __str__(self):
        return f'chambre N-{self.id}'
    
class Reservation(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reserve")
    chambre=models.ForeignKey(Chambre,on_delete=models.CASCADE,related_name="chambre_reserve")
    Date_debut = models.DateField(auto_now=False)
    Date_fin = models.DateField(auto_now=False)
    def __str__(self):
        return f'{self.client} - {self.chambre}'

class Facture(models.Model):
    reservation=models.OneToOneField(Reservation,on_delete=models.CASCADE)
    PAY_TYPE = (('cach', 'cach'), ('card', 'card'),)
    Date_facteur = models.DateField(auto_now=True)
    mode_payment=models.CharField(max_length=120,choices=PAY_TYPE,default="card")
    def __str__(self):
        return str(self.reservation) 

