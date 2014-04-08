# -*- coding:utf-8 -*- 

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'playlists.views',

    url(r'^$', 'index'),
    url(r'^(?P<pk>\d+)/$', 'playlist'),
)
