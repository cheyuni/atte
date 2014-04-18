# -*- coding:utf-8 -*- 
from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.utils.translation import ugettext_lazy as _
# from django.utils import timezone
# from django.contrib.auth.hashers import make_password, check_password
# from core.models import AtteModel

# class UserManager(BaseUserManager):
#     def create_user(self, user_id, password=None, **extra_arguments):
#         """
#         creates user with email and password
#         """
#         now = timezone.now()
#         user = self.model(
#             user_id=user_id, is_staff=False, is_active=True, is_superuser=False,
#             last_login_date=now, **extra_arguments
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_id, password, **extra_fields):
#         su = self.create_user(user_id, password, **extra_fields)
#         su.is_active = True
#         su.is_staff = True
#         su.is_superuser = True
#         su.save(using=self._db)
#         return su


# class AtteAbstractUser(AbstractBaseUser, PermissionsMixin):
#     MALE = 'M'
#     FEMALE = 'F'

#     MALE_FEMALE_CHOICES = (
#         (MALE, u'남'),
#         (FEMALE, u'여')
#     )

#     is_active = models.BooleanField(default=True)
#     name = models.CharField(_(u'이름'), 
#                                  max_length=15, 
#                                  help_text=_(u'이름'))
    
#     user_id = models.CharField(_(u'아이디'), 
#                                max_length=15, 
#                                help_text=_(u'사용자 아이디'),
#                                unique=True,
#                                db_index=True)
    
#     sex = models.CharField(_(u'성별'), max_length=1,
#                            choices=MALE_FEMALE_CHOICES,
#                            default='M')
    
#     age = models.IntegerField(_(u'나이'), blank=True, null=True)
    
#     email = models.EmailField(_('Email'),
#                               max_length=255,
#                               db_index=True,
#                               unique=True)

#     last_login_date = models.DateTimeField(_('last login'), default=timezone.now)

#     USERNAME_FIELD = 'user_id'
#     REQUIRED_FIELDS = ['name']

#     objects = UserManager()
    
#     def get_full_name(self):
#         return self.name

#     def get_username(self):
#         return self.name

#     def get_short_name(self):
#         return self.name
    
#     def get_email(self):
#         return self.email
                                               
#     class Meta:
#         abstract = True

#     def __unicode__(self):
#         return self.name

# class User(AtteAbstractUser):
#     is_staff = models.BooleanField(_('staff status'),
#                                    default=False,
#                                    help_text=_('Designates whether the user can log into this admin'))
    
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
        
#     def check_password(self, raw_password):
#         """
#         Returns a boolean of whether the raw_password was correct. Handles
#         hashing formats behind the scenes.
#         """
#         def setter(raw_password):
#             self.set_password(raw_password)
#             self.save(update_fields=["password"])
#         return check_password(raw_password, self.password, setter)

#     class Meta:
#         verbose_name = _(u'아떼 유저')
#         verbose_name_plural = _(u'아떼 유저들')


# class SocialUser(AbstractBaseUser):
#     class Meta:
#         verbose_name = _(u'소셜 유저')
#         verbose_name_plural = _(u'소셜 유저들')
    
