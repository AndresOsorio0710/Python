from django.urls import path
from beauty_public_area_app.views.register_user import RegisterUserView

urlpatterns =[
    path('pl-signin', RegisterUserView.beauty_public_register_user, name='beauty_public_register_user'),
]