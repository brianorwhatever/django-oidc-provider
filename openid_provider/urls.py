from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

from openid_provider.views import *


urlpatterns = patterns('',
                       url(r'^authorize/$', AuthorizeView.as_view(), name='authorize'),
                       url(r'^token/$', csrf_exempt(TokenView.as_view()), name='token'),
                       url(r'^userinfo/$', csrf_exempt(userinfo), name='userinfo'),

)