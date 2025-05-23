from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.chat_view,name='chat'),
    path('chat/api',views.chat_api,name='chat_api')
    ]