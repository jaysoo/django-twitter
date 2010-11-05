# Adopted from python-twitter's get_access_key.py # http://code.google.com/p/python-twitter/

import urllib, urllib2
import oauth2 as oauth
import twitter

try:
    from urlparse import parse_qsl
except:
    from cgi import parse_qsl

from django.conf import settings

from models import TwitterAccount

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL    = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL                = 'https://api.twitter.com/oauth/authenticate'

consumer_key = settings.TWITTER_CONSUMER_KEY
consumer_secret = settings.TWITTER_CONSUMER_SECRET

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
oauth_client = oauth.Client(oauth_consumer)

def get_request_token():
    resp, content = oauth_client.request(REQUEST_TOKEN_URL, 'GET')
    if resp['status'] == '200':
        return dict(parse_qsl(content))

def get_authorization_url(request_token):
    return '%s?oauth_token=%s' % (AUTHORIZATION_URL, request_token['oauth_token']),

def get_access_token(request_token, pincode):
    token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(pincode)

    oauth_client = oauth.Client(oauth_consumer, token)
    resp, content = oauth_client.request(ACCESS_TOKEN_URL, method='POST', body='oauth_verifier=%s' % pincode)
    access_token = dict(parse_qsl(content))

    if resp['status'] == '200':
        return access_token
