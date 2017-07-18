from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.org, name='org_view'),
	url(r'^datael/', views.datael, name='datael'),
	url(r'^map/', views.map, name='org_map'),
	url(r'^charts/', views.analytics, name='analytics'),
	url(r'^analytics_data/', views.analytics_data, name='analytics_data'),
	url(r'^preg_data/', views.preg_comp, name='preg_data'),

]
