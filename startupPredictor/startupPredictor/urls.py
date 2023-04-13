"""startupPredictor URL Configuration
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('roi/', my_view, name='roi'),
    path('api/', predict, name='model'),
    path('home/', homepage, name='home'),
    path('', homepage, name='home'),
    path('results/', results_view, name='results_view'),
]
