from django.db import models

# Create your models here.
class chat(models.Model):
    message = models.CharField(max_length=1000, blank=True)
    sender = models.CharField(max_length=5, blank=True)
    chat_owner =  models.CharField(max_length=100, blank=True)
    time =  models.CharField(max_length=20, blank=True)

class bot_reply(models.Model):
    answer = models.CharField(max_length=1000, blank=True)
    keyword1 = models.CharField(max_length=100, blank=True)
    keyword2 =  models.CharField(max_length=100, blank=True)
    keyword3 =  models.CharField(max_length=100, blank=True)
