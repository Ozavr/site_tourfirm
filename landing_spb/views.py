from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_managers
from app import settings

# Our model
from landing_spb.models import RequestSpb

class LandingView(CreateView):
	'''
	Controller for creating requests of the clients to our managers
	Контроллер для создания запроса клиетов для наших менеджеров
	'''
	model = RequestSpb
	template_name = 'landing_spb.html'
	fields = [ 'name', 'phone', 'email' ]
	success_url = reverse_lazy( 'spb_success' )

	def form_valid( self, form ):
		'''
		sending the email request
		'''
		output = super( LandingView, self ).form_valid( form )

		# Creating message for the managers
		request_message = 'Запрос клиента с сайта tagilturist.ru/!\n'
		request_message += 'Санкт-Петербург тур "Все включено"\n'
		request_message += 'Имя: ' + form.instance.name + '\n'
		request_message += 'Телефон: ' + form.instance.phone + '\n'
		request_message += 'email: ' + form.instance.email + '\n'

		mail_managers( 'Запрос клиента в Санкт-Петербург', request_message )
		return output 

class SuccessMessage( TemplateView ):
	"""docstring for SuccessMessage"""
	template_name = 'landing_spb_success.html'