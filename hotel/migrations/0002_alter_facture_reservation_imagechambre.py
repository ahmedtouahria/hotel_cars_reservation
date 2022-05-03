# Generated by Django 4.0.4 on 2022-05-02 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='reservation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel.reservation'),
        ),
        migrations.CreateModel(
            name='ImageChambre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/chambre')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.chambre')),
            ],
        ),
    ]