from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

try:
    import json
except:
    import simplejson as json

from utils import *

@login_required
def authorize(request):
    token = get_request_token()
    url = get_authorization_url(token)
    request.session['request_token'] = token
    return HttpResponseRedirect(url)

@login_required
def access_token(request):
    if request.method == 'GET':
        oauth_verifier = request.GET['oauth_verifier']
        request_token = request.session['request_token']
        access_token = get_access_token(request_token, oauth_verifier)
        print access_token
        return render_to_response('django_tweet/success.html', {
            'screen_name': access_token['screen_name'],
            'oauth_token': access_token['oauth_token'],
            'oauth_token_secret': access_token['oauth_token_secret'],
        })

