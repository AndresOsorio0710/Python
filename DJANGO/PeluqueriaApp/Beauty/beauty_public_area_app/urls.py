from django.urls import path, include

urlpatterns = [
    path('', include('beauty_public_area_app.url.home')),
    path('', include('beauty_public_area_app.url.register_user')),
]