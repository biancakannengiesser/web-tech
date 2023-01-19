from django.contrib import admin
from .models import Service
from .models import Appointment

#admin.site.register(Service)
#admin.site.register(Appointment)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):			#modify admin area
	list_display = ('service', 'price', 'employee')			#what attributes to display
	ordering = ('service',)						#order by service
	search_fields = ('service', 'employee')		#inlcude search bar

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name','service', 'date')	
	ordering = ('service',)	
	search_fields = ('service', 'first_name', 'last_name')