from django.urls import path
from beauty_public_area_app.views.home import beauty_public_home

urlpatterns =[
    path('', beauty_public_home, name='beauty_public_home'),
]