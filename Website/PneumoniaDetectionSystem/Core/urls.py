from django.urls import path
from Core.views import*

urlpatterns = [
    path('', homePage, name='home'),
    path('result/', result, name='result'),
    path('about-us/', about, name='about'),
    path('faqs/', faqs, name='faqs'),
    path('privacy/', privacy, name='privacy'),
    path('contact-us/', contact, name='contact'),
    path('terms-and-conditions/', terms, name='terms')

    
    # Other URL patterns for the core app
]
