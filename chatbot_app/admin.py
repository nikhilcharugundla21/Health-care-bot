from django.contrib import admin

# Register your models here.
from .models import chat
from .models import bot_reply

admin.site.register(chat)
admin.site.register(bot_reply)
