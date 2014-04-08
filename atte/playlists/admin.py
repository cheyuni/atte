from django.contrib import admin
from playlists.models import Playlist, Video

class PlaylistAdmin(admin.ModelAdmin):
    list_filter = ('is_best',)
    search_fields = ('title',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('query', 'playlist')
    search_fields = ('query', 'playlist__title')

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video, VideoAdmin)
