# Generated by Django 4.0.4 on 2022-05-04 14:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('type_car', models.CharField(max_length=12)),
                ('prix', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media/car/')),
                ('disponibilité', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_debut', models.DateField()),
                ('Date_fin', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='cars.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve_car', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FactureCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_facteur', models.DateField(auto_now=True)),
                ('mode_payment', models.CharField(choices=[('cach', 'cach'), ('card', 'card')], default='card', max_length=120)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.reservationcar')),
            ],
        ),
    ]