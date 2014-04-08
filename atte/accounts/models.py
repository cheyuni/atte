# -*- coding:utf-8 -*- 

# rpxnow.com의 설정에 따라 바뀔 수 있음.

from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class User(models.Model):
    provider = models.ForeignKey(Provider)
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
