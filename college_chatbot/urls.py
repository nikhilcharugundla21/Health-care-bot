from django.contrib import admin
from django.urls import path
from chatbot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.chat_view.as_view()),
    path('ajax/crud/create/',  views.send_chatdata.as_view(), name='send_c'),
]
