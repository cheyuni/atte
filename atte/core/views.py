# -*- coding:utf-8 -*-
import json

from apiclient.discovery import build
from optparse import OptionParser

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

DEVELOPER_KEY = "AIzaSyCNqDHPcknvtKkae693fAdNmJfoDjZsKxQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search(search_string):
  parser = OptionParser()
  parser.add_option("--q", dest="q", help="Search term",
    default = search_string)
  parser.add_option("--max-results", dest="maxResults",
    help="Max results", default=1)
  (options, args) = parser.parse_args()    
  
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.maxResults
  ).execute()

  video_id = None
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      video_id = "%s" % search_result["id"]["videoId"]
      # title = search_result['snippet']['title']

  return video_id
  # return dict(video_id=video_id, title=title)

@ensure_csrf_cookie
def index(request):
    # playlist = Playlist.objects.all()[:20]
    return render(request, r'index.html')#, dict(playlist=playlist))

def get_video(request):
    if request.is_ajax():
        if 'query' not in request.POST:
            return HttpResponse("bad request")
        else:
            search_string = request.POST['query']
            return HttpResponse(youtube.search(search_string))
    else :
        return HttpResponse("bad request")

def get_music_list(request):
    if request.is_ajax():
        if 'query' not in request.POST:
            return HttpResponse("bad request")
        else:
            list_id = request.POST['query']
            music_list = Playlist.objects.get(id=int(list_id)).music_set.all()
            data = {}
            music_infos = []
            for i in music_list:
                data_set = []
                data_set.append(i.id)
                data_set.append(i.name)
                music_infos.append(data_set)

            data['title'] = Playlist.objects.get(id=int(list_id)).name
            data['music_infos'] = music_infos
            return HttpResponse(json.dumps(data))
    else :
        return HttpResponse("bad request")

def update_music(request):
    if request.is_ajax():
        if 'query' not in request.POST:
            return HttpResponse("bad request")
        else:
            if 'update_value' not in request.POST:
                return HttpResponse("bad request")
            else:
                if 'status' not in request.POST:
                    return HttpResponse("bad request")
                else:
                    if request.POST['status'] == 'update':
                        music_id = request.POST['query']
                        music = Music.objects.get(id=music_id)
                        music.name = request.POST['update_value']
                        music.save()
                        return HttpResponse(music.name)
                    elif request.POST['status'] == 'add':
                        playlist_id = request.POST['query']
                        playlist = Playlist.objects.get(id=playlist_id)
                        added_music = playlist.music_set.create(name=request.POST['update_value']);
                        added_music.save()
                        data = {}
                        data['id'] = added_music.id
                        data['name'] = added_music.name
                        return HttpResponse(json.dumps(data))
                    else:
                        return HttpResponse('bas request')
    else :
        return HttpResponse("bad request")

def delete_music(request):
    if request.is_ajax():
        if 'query' not in request.POST:
            return HttpResponse("bad request")
        else:
            music = Music.objects.get(id=request.POST['query'])
            music.delete()
            return HttpResponse("success")
    else :
        return HttpResponse("bad request")

def update_playlist(request):
    if request.is_ajax():
        if 'playlist_id' not in request.POST:
            return HttpResponse("bad request")
        else:
            if 'update_value' not in request.POST:
                return HttpResponse("bad request")
            else:
                playlist_id = request.POST['playlist_id']
                playlist = Playlist.objects.get(id=playlist_id)
                update_value = request.POST['update_value']
                playlist.name = update_value
                playlist.save()
                return HttpResponse(playlist.name)
    else :
        return HttpResponse("bad request")

def add_playlist(request):
    if request.is_ajax():
        if 'name' not in request.POST:
            return HttpResponse("bad request")
        else:
            playlist_name = request.POST['name']
            playlist = Playlist.objects.create(name=playlist_name)
            playlist.save()
            data = {'id':playlist.id, 'name':playlist.name}
            return HttpResponse(json.dumps(data))
    else :
        return HttpResponse("bad request")

def delete_playlist(request):
    if request.is_ajax():
        if 'playlist_id' not in request.POST:
            return HttpResponse("bad request")
        else:
            playlist_id = request.POST['playlist_id']
            playlist = Playlist.objects.get(id=playlist_id)
            playlist.delete()
            data = "success"
            return HttpResponse(data)
    else :
        return HttpResponse("bad request")


def search_playlist(request):
    if request.is_ajax():
        if 'name' not in request.POST:
            return HttpResponse("bad request")
        else:
            name = request.POST['name']
            lists = Playlist.objects.all().filter(name__contains=name)
            data_set = []
            for i in lists:
                data = {}
                data['name'] = i.name
                data['id'] = i.id
                data_set.append(data)
            return HttpResponse(json.dumps(data_set))
    else :
        return HttpResponse("bad request")  
