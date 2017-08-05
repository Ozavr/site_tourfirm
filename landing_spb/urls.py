from django.conf.urls import url

#Our controllers
from landing_spb.views import LandingView, SuccessMessage

urlpatterns = [
	url( r'^$', LandingView.as_view(), name = 'landing_spb' ),
	url( r'^success/$', SuccessMessage.as_view(), name = 'spb_success' ),
]
