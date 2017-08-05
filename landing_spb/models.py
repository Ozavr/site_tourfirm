from django.db import models

# Create your models here.

class RequestSpb( models.Model ):
	'''
	List of request to get the good
	Список желающих получить информацию о товаре
	'''

	name = models.CharField( max_length = 20, verbose_name = 'Имя' )
	phone = models.CharField( max_length = 20, verbose_name = 'Номер телефона' )
	email = models.CharField( max_length = 20, verbose_name = 'email', blank = True )
	date = models.DateTimeField( auto_now_add = True, db_index = True )

	class Meta:
		'''
		Settings for the model
		Настройки модели
		'''
		ordering = [ '-date' ]
		verbose_name = 'Список запросов в spb'
		verbose_name_plural = 'Список запросов в spb'