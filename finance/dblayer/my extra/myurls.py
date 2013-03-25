from django.conf.urls.defaults import*
urlpatterns = patterns('dblayer.views',
    url(r'^f/(\d)/$', 'dataFetch'),
    url(r'^show/$','archive'),
    url(r'^create/$', 'formDB')
)
