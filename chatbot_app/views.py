from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import View
from .models import chat
from .models import bot_reply
from django.http import JsonResponse
from django.db.models import Q
import bot

class chat_view(ListView):
    model = chat
    template_name = 'chat_bot/index.html'
    context_object_name = 'chat_data'

class send_chatdata(View):
    def  get(self, request):
        chat_msg_user = request.GET.get('chat_msg', None)
        login_user = request.GET.get('login_user', None)
        chat_time = "5:44"
        
        bot_aa=bot.chat(chat_msg_user)
        print(chat_msg_user,bot_aa)
        bot_uttar = bot_reply.objects.filter(Q(keyword1__icontains=chat_msg_user) |
                                             Q(keyword2__icontains=chat_msg_user) |
                                             Q(keyword3__icontains=chat_msg_user)
                                            )
        for b_a in bot_uttar:
            if b_a.answer:
                bot_aa=b_a.answer


        obj1 = chat.objects.create(
            message = bot_aa,
            sender = 'bot',
            chat_owner = login_user,
            time = chat_time
            )
        obj = chat.objects.create(
            message = chat_msg_user,
            sender = 'user',
            chat_owner = login_user,
            time = chat_time
        )

        all_data = {'id':obj.id,'chat_msg':obj.message,'message_sender':obj.sender,'login_user':obj.chat_owner,'chat_time':obj.time,'bot_reply1':bot_aa}

        data = {
            'chat_data': all_data
        }
        return JsonResponse(data)
