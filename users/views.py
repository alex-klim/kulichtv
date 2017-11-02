from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, TemplateView, FormView, ListView, UpdateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

import oauth2 as oauth
from urllib.parse import parse_qsl
import pickle

from .models import *
from core.settings import consumer_key, consumer_secret, request_token_url, access_token_url, authenticate_url
from .backend import CustomBackend


consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

class UserLoginView(FormView):
    template_name = 'users/login.html'
    model = CustomUser
    # form_class = AuthentificationForm

    def form_valid(self, form):
        form.save()
        return super(CommunityAddView, self).form_valid(form)

    
class UserRegistrationView(FormView):
    template_name = 'users/registration.html'
    model = CustomUser
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super(CommunityAddView, self).form_valid(form)

def twitter_login(request):
    if request.user.is_active:
        HttpResponseRedirect('/index')

    # Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    # Store the request token in a session for later use.
    request.session['request_token'] = {k.decode('utf8'): v.decode('utf8') for k, v in dict(parse_qsl(content)).items()}

    # Redirect the user to the authentication URL.
    url = "%s?oauth_token=%s" % (authenticate_url,
        request.session['request_token']['oauth_token'])

    return HttpResponseRedirect(url)

def twitter_authenticated(request):
    # Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token']['oauth_token'],
        request.session['request_token']['oauth_token_secret'])
    token.set_verifier(request.GET['oauth_verifier'])
    client = oauth.Client(consumer, token)

    # Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        print(content)
        raise Exception("Invalid response from Twitter.")

    access_token = {k.decode('utf8'): v.decode('utf8') for k, v in dict(parse_qsl(content)).items()}
    print(access_token)

    try:
        user = CustomUser.objects.get(nickname=access_token['screen_name'])
    except CustomUser.DoesNotExist:
        # When creating the user I just use their screen_name@twitter.com
        # for their email and the oauth_token_secret for their password.
        # These two things will likely never be used. Alternatively, you 
        # can prompt them for their email here. Either way, the password 
        # should never be used.
        user = CustomUser.objects.create_user(access_token['screen_name'])

        user.oauth_token = access_token['oauth_token']
        user.oauth_secret = access_token['oauth_token_secret']
        user.save()
    
    # Authenticate the user and log them in using Django's pre-built 
    # functions for these things.
    user = authenticate(nickname=access_token['screen_name'])
    print(user)
    login(request, user)
    print(user.is_authenticated())

    return HttpResponseRedirect('/index/')

@login_required
def dismissed(request):
    logout(request)
    return HttpResponseRedirect('/index/')
