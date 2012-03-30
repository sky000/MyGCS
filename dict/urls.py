from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'dict.index.main'),
	url(r'^host/$', 'dict.hosts.list'),
	url(r'^host/(?P<host_id>\d+)/$', 'dict.hosts.detail'),
	url(r'^instance/(?P<instance_id>\d+)/$', 'dict.instance.detail'),
	url(r'^host/(?P<host_id>\d+)/update/$', 'dict.hosts.update'),
	#url(r'^(?P<hostname>.*?)/instance/$', 'show.views.instances'),
	#url(r'^(?P<hostname>.*?)/database/$', 'show.views.databases'),
	#url(r'^(?P<hostname>.*?)/(?P<database>.*?)/schema/$', 'show.views.schemas'),
)
