from .admins import *
from .models import *
from django.contrib import admin

admin.site.register(Person, PersonAdmin)
