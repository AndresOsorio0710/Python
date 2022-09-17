from django.urls import path, include

urlpatterns = [
    path('', include('authentication_app.url.token')),
    path('', include('authentication_app.url.user')),
    path('', include('authentication_app.url.logout')),
]