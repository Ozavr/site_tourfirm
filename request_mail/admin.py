from django.contrib import admin
from request_mail.models import RequestList

class RequestlistAdmin( admin.ModelAdmin ):
	'''
	Class for display the list of request in the admin panel
	'''
	list_display = ( 'date', 'country', 'data_sending', 'days', 'people', 'food', 'price', 'name', 'phone', 'email', 'description', )
	search_fields = ( 'name', 'phone' )
	

admin.site.register( RequestList, RequestlistAdmin )

# Register your models here.