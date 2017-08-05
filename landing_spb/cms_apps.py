from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class LandingApp(CMSApp):
	app_name = 'Landing'
	name = _("Landing App") # give your app a name, this is required
	
	def get_urls( self, page = None, language = 'ru', **kwargs ):
		return [ 'landing_spb.urls' ]

apphook_pool.register(LandingApp) # register your app