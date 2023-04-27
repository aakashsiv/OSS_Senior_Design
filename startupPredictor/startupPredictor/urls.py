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
    path('contactUs/', contact_view, name='contactUs'),
    path('contactUs/success/', contact_success, name='contact_success'),
    path('topPicks/', top_picks, name='topPicks'),
    path('autocomplete-org-names/', autocomplete_org_names, name='autocomplete_org_names'),
    path('more-details/', get_more_details, name='details'),
    path('details/<int:id>/', organization_details, name='detailsID'),
]