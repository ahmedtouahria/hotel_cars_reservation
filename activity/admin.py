from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Activity)
admin.site.register(ReservationActivity)
admin.site.register(FactureActivity)

admin.site.unregister(Group)