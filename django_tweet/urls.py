from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^authorize/$', authorize, name='tweet-authorize'),
    url(r'^access/$', access_token, name='tweet-access-token'),
)
