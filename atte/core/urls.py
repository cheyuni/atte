from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
                       url(r'^$', 'index'),
                       url(r'^get_video$', 'get_video'),
                       url(r'^get_music_list$', 'get_music_list'),
                       url(r'^update_music$', 'update_music'),
                       url(r'^delete_music$', 'delete_music'),
                       url(r'^update_playlist$', 'update_playlist'),
                       url(r'^add_playlist$', 'add_playlist'),
                       url(r'^delete_playlist$', 'delete_playlist'),
                       url(r'^search_playlist$', 'search_playlist'),
)


