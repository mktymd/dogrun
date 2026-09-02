from django.contrib import admin
from dogruns.models import  Profile
admin.site.register(Profile)
from .models import DogRun
admin.site.register(DogRun)
# Register your models here.
