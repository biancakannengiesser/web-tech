from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    # path('appointment', views.appointment, name='appointment'),
    path('make_appointment', views.make_appointment, name='make_appointment'),
    path('price', views.price, name='price'),
]
