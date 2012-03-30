from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/templates/statics/'}),
    url(r'^$', 'MyGCS.index.main', name='home'),
    url(r'^sys/', include('MyGCS.dict.urls')),
    url(r'^perf/', include('MyGCS.perf.urls')),
    url(r'^backup/', include('MyGCS.backup.urls')),
    url(r'^setup/', include('MyGCS.setup.urls')),
	#url(r'^p/', include('myops.perf.urls')),


)
urlpatterns += staticfiles_urlpatterns()