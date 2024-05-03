from django.urls import path
from Core.views import*

urlpatterns = [
    path('', homePage, name='home'),
    path('result/', result, name='result'),
    # Other URL patterns for the core app
]
