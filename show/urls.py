from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^host/$', 'show.host.list_hosts'),
	url(r'^(?P<hostname>.*?)/instance/$', 'show.views.instances'),
	url(r'^(?P<hostname>.*?)/database/$', 'show.views.databases'),
	url(r'^(?P<hostname>.*?)/(?P<database>.*?)/schema/$', 'show.views.schemas'),
)
