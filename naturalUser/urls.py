from django.urls import path
from .views import IndexView, LoginView, RegisterFormView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('autentificacion', LoginView.as_view(), name='login'),
    path('registro', RegisterFormView.as_view(), name='register')
]