from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^authorize/$', authorize, name='twitter-authorize'),
    url(r'^access/$', access_token, name='twitter-access-token'),
)
