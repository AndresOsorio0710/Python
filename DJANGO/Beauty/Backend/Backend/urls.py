from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/login/', views.obtain_auth_token),
    path('api/1.0/', include('authentication_app.urls')),
    path('api/1.0/', include('person_app.urls')),
]
