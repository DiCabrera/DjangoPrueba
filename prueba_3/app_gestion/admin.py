from atexit import register
from django.contrib import admin

# Register your models here.
from app_gestion.models import Persona
admin.site.register(Persona)
