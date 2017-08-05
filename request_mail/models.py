from django.db import models
# from cms.models import CMSPlugin

class RequestList( models.Model ):
	'''
	Model of the list clients request 
	Модель базы данных для базы данных в которую записываются данные клиента при запросе
	'''
	country = models.CharField( max_length = 35, verbose_name = 'Страна отправления', blank = True )
	data_sending = models.CharField( max_length = 35, verbose_name = 'Дата поездки', blank = True )
	days = models.CharField( max_length = 20, verbose_name = 'Продолжительность поездки', blank = True )
	people = models.CharField( max_length = 140, verbose_name = 'Колличество человек', blank = True )
	food = models.CharField( max_length = 140, verbose_name = 'Питание', blank = True )
	price = models.CharField( max_length = 35, verbose_name = 'Цена', blank = True )
	name = models.CharField( max_length = 20, verbose_name = 'Имя' )
	phone = models.CharField( max_length = 20, verbose_name = 'Номер телефона' )
	email = models.CharField( max_length = 20, verbose_name = 'email', blank = True ) #
	description = models.TextField( max_length = 768, verbose_name = 'Краткое содержание вашей заявки', blank = True )
	date = models.DateTimeField( auto_now_add = True, db_index = True )

	class Meta:
		'''
		Settings for the model
		'''
		ordering = [ '-date' ]
		verbose_name = 'Список запросов'
		verbose_name_plural = 'Список запросов'