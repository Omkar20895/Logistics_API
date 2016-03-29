from django.conf.urls import include, url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from logistics_api import views

urlpatterns = patterns('',
		url(r'^api/$', views.DriverList.as_view()),
		url(r'^api/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view())
	)


urlpatterns = format_suffix_patterns(urlpatterns)