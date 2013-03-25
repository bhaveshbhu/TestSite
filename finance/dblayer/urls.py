from django.conf.urls.defaults import*
urlpatterns = patterns('dblayer.views',
    url(r'^f/$', 'dataFetch'),
)
