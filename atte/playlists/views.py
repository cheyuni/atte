# -*- coding:utf-8 -*- 

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from playlists.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

def index(request):
    return playlist(request, 1)

def playlist(request, pk):
    try:
        playlist = Playlist.objects.get(pk=pk)
        print dir((RequestContext(request)))
        return render(request, 'playlist.html', dict(playlist=playlist))
    except ObjectDoesNotExist:
        # FIXME : 잘못된 playlist pk가 들어왔을때
        return HttpResponseRedirect('/')
