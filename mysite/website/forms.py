from django import forms
from django.forms import ModelForm
from .models import Appointment

class AppointmentForm(ModelForm):
	class Meta:						#allows you to KINDA(?) define the things in a class for django
		model = Appointment
		#fields = "__all__"			if you want all the fields from the class Appointment
		fields = ('last_name', 'first_name', 'email', 'phone', 'service', 'date')
		labels = {
			'last_name': '',
			'first_name': '',
			'email': '',
			'phone': '',
			'service': 'Service',
			'date': 'YYYY-MM-DD HH:MM:SS',
			}
		
		widgets = {
			'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
			"first_name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
			"email": forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
			"phone": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}),
			"service": forms.Select(attrs={'class':'form-select', 'placeholder': 'Service'}),
			"date": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Date'}),
		}