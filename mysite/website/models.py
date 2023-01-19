from django.db import models


# class Employee(models.Model):
# 	first_name = models.CharField(max_length = 30)
# 	last_name = models.CharField(max_length = 30)
# 	phone = models.CharField("Mobile number", max_length = 10)
# 	email_address = models.EmailField("Email address")

# 	def __str__(self):
# 		return self.first_name + " " + self.last_name

class Service(models.Model):
	service = models.CharField("Service", max_length = 120)
	price = models.IntegerField("Price")
	employee = models.CharField("Employee", max_length = 60)
	description = models.TextField(blank = True)

	def __str__(self):
		return self.service

class Appointment(models.Model):
	last_name = models.CharField("Last name", max_length = 120)
	first_name = models.CharField("First name", max_length = 120)
	email = models.EmailField("Email address")
	phone = models.CharField("Mobile number", max_length = 10)
	service =  models.ForeignKey(Service, null = True, on_delete = models.CASCADE)
	date = models.DateTimeField("Appointment Date")

	def __str__(self):
		return self.last_name + " " + self.first_name