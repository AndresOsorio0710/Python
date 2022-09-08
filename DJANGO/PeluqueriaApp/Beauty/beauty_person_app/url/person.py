from django.urls import path
from beauty_person_app.views import PersonView

urlpatterns =[
    path('ps-signin/', PersonView.person_register, name='person_register'),
]