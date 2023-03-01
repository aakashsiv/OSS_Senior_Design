from django.urls import path
from .views import my_view, predict

urlpatterns = [
    path('', my_view, name='home'),
    path('api/', predict, name='model')
]
