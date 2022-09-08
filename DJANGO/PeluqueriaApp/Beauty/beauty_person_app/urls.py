from django.urls import path, include

urlpatterns = [
    path('', include('beauty_person_app.url.person')),
    path('api/', include('beauty_person_app.url.person_api')),
]