# -*- coding:utf-8 -*- 

from django.db import models
from accounts.models import User

# Playlist.objects 로 시작하는 query는 is_best가 항상 False
class NormalPlaylistManager(models.Manager):
    def get_query_set(self):
        return super(NormalPlaylistManager, self).get_query_set().filter(is_best=False)

# Playlist.best_objects 로 시작하는 query는 is_best가 항상 True
class BestPlaylistManager(models.Manager):
    def get_query_set(self):
        return super(BestPlaylistManager, self).get_query_set().filter(is_best=True)

class Playlist(models.Model):
    user = models.ForeignKey(User)
    subscriber = models.ManyToManyField(User, related_name='subscription_set', blank=True)
    title = models.CharField(max_length=256)
    is_best = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)

    # managers
    objects = models.Manager()            # default
    normal_objects = NormalPlaylistManager()
    best_objects = BestPlaylistManager()

    def __unicode__(self):
        return self.title

    # 일반 Playlist를 Best Playlist로 바꾸면 그 유저의 기존의 Best Playlist는 자동으로 일반 Playlist로 바뀌도록 override
    def save(self, *args, **kwargs):
        if self.is_best == True:
            Playlist.objects.filter(user=self.user, is_best=True).update(is_best=False)
        super(Playlist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '플레이리스트'
        verbose_name_plural = '플레이리스트들'

class Video(models.Model):
    playlist = models.ForeignKey(Playlist)
    query = models.CharField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.query

    class Meta:
        verbose_name = '비디오'
        verbose_name_plural = '비디오들'
