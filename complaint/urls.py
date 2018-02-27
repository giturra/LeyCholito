from django.urls import path
from .views import ComplaintFormView


urlpatterns = [
    path('', ComplaintFormView.as_view(), name='index'),
]