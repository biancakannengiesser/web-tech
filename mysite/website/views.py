from django.shortcuts import render
from .models import Service
from .forms import AppointmentForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def index(request):
	return render(request, 'index.html', {})

def services(request):
	return render(request, 'services.html', {})

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		mess = request.POST['mess']

		send_mail(
			'Message From Customer',		# email subject
			mess,							# message to be sent(from customer)
			email,							# customers email
			['biakannengiesser@gmail.com'],			# receiver of the email 
			)

		return render(request, 'contact.html', {'mess_name': name})
	else:
		return render(request, 'contact.html', {})

# def appointment(request):
# 	services = Service.objects.all()
# 	return render(request, 'appointment.html', {'services': services})

def make_appointment(request):
	services = Service.objects.all()
	submitted = False
	if request.method == "POST":
		form = AppointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/make_appointment?submitted=True')
	else:
		form = AppointmentForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, 'make_appointment.html', {'form': form, 'submitted': submitted, 'services':services})

def price(request):
	services = Service.objects.all()
	return render(request, 'price.html', {'services': services})