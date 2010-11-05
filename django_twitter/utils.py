# Adopted from python-twitter's get_access_key.py # http://code.google.com/p/python-twitter/

import urllib, urllib2
import oauth2 as oauth
import twitter

try:
    import json
except:
    import simplejson as json

try:
    from urlparse import parse_qsl
except:
    from cgi import parse_qsl

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.http import HttpResponse

from models import TwitterAccount

USER_URL = 'http://api.twitter.com/1/users/show/%s.json'
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
oauth_consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
oauth_client = oauth.Client(oauth_consumer)

def get_request_token():
    current_site = Site.objects.get_current()
    callback_url = 'http://%s%s' % (current_site.domain, reverse('twitter-access-token'))
    resp, content = oauth_client.request(REQUEST_TOKEN_URL, 'POST', 'oauth_callback=%s' % callback_url)
    if resp['status'] == '200':
        return dict(parse_qsl(content))
    return HttpResponse('Oops, something borked', mimetype='text/plain', status=500)

def get_authorization_url(request_token):
    return '%s?oauth_token=%s' % (AUTHORIZATION_URL, request_token['oauth_token'])

def get_access_token(request_token, oauth_verifier):
    token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    oauth_client = oauth.Client(oauth_consumer, token)
    resp, content = oauth_client.request(ACCESS_TOKEN_URL, method='POST', body='oauth_verifier=%s' % oauth_verifier)
    access_token = dict(parse_qsl(content))

    if resp['status'] == '200':
        return access_token

def get_image_url(username):
    result = json.load(urllib.urlopen(USER_URL % username))
    return result['profile_image_url']

