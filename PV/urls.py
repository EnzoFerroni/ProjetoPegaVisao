from django.urls import path
from PV.views import index

urlpatterns = [
    path('', index),
]
