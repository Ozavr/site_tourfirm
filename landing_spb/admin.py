from django.contrib import admin
from landing_spb.models import RequestSpb

class RequestSpbAdmin( admin.ModelAdmin ):
	'''
	Class for display the list of request in the admin panel
	'''
	list_display = ( 'date', 'name', 'phone', 'email', )
	search_fields = ( 'name', 'phone' )
	

admin.site.register( RequestSpb, RequestSpbAdmin )