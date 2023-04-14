
from django.urls import path
from .views import VRegistro, salir, loginn

urlpatterns = [

    path('registro/', VRegistro.as_view(), name='registro'),
    path('sd/', salir, name='salir1'),
    path('login/', loginn, name='login'),
]
