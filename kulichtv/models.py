import os

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):

    def get_pic_url(instance, filename):
        return os.path.join('profiles', str(instance.nickname), filename)
    
    nickname = models.CharField(max_length=40)
    pic = models.ImageField(upload_to=get_pic_url, default='None/none.jpg')

    def __str__(self):
        return self.nickname


class Game(models.Model):

    def get_pic_url(instance, filename):
        return os.path.join('games', str(instance.title)+'.jpg')
    
    title = models.CharField(max_length=40, blank=False)
    descr = models.TextField(max_length=275)
    pic = ProcessedImageField(upload_to=get_pic_url,
                                           processors=[ResizeToFill(300, 150)],
                                           format='JPEG',
                                           options={'quality': 60})

    def __str__(self):
        return self.title


class Community(models.Model):
    name = models.CharField(max_length=50, blank=False)
    descr = models.TextField(max_length=500)
    rules = models.TextField(max_length=300)

    class Meta:
        verbose_name_plural = "Communities"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/communities/%i/" % self.pk


# class Stream(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     communities = models.ManyToManyField(Community)
