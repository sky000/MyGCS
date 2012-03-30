from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/templates/statics/'}),
    url(r'^$', 'myops.index.main', name='home'),
    url(r'^sys/', include('myops.dict.urls')),
	#url(r'^p/', include('myops.perf.urls')),


)
urlpatterns += staticfiles_urlpatterns()