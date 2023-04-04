# """Important lines when importing a model in consumers.py file"""
import os
import django
from channels.db import database_sync_to_async
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')
django.setup()


from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

from .models import Messagge
from django.contrib.auth.models import User

from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MyAsyncConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_chat(self, message, sender):
        user_obj = User.objects.get(username=sender)
        return Messagge.objects.create(context=message, sender=user_obj)
    
    async def connect(self):
        print("inside connect")
        self.roomGroupName = 'chat-group'

        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        
        await self.accept()
        
    async def disconnect(self, close_code):
        print("inside disconnect")
        raise StopConsumer()
        
    async def receive(self, text_data):
        print("inside receive")
        text_data_json = json.loads(text_data)                  #loads() = string of json type --to--> json object
        
        message = text_data_json['message']
        username = text_data_json['username']
        firstname = text_data_json['firstname']
        
        obj = await self.save_chat(message, username)
        
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message ,
                "firstname" : firstname ,
            })
        
    async def sendMessage(self, event):
        print("inside sendmessage")
        message = event["message"]
        firstname = event["firstname"]
        
        # obj = await self.save_chat(message, username)
        
        await self.send(text_data = json.dumps({'message':message, 'firstname':firstname}))     #dumps() = json object --to--> string of json type


# class MyAsyncConsumer(AsyncWebsocketConsumer):
    
#     async def connect(self):
#         print("inside connect")
#         self.roomGroupName = 'chat-group'

#         await self.channel_layer.group_add(
#             self.roomGroupName,
#             self.channel_name
#         )
        
#         await self.accept()
        
#     async def disconnect(self, close_code):
#         print("inside disconnect")
#         raise StopConsumer()
        
#     async def receive(self, text_data):
#         print("inside receive")
#         text_data_json = json.loads(text_data)                  #loads() = string of json type --to--> json object
        
#         message = text_data_json['message']
#         username = text_data_json['username']
        
#         await self.channel_layer.group_send(
#             self.roomGroupName,{
#                 "type" : "sendMessage" ,
#                 "message" : message ,
#                 "username" : username ,
#             })
        
#     async def sendMessage(self, event):
#         print("inside sendmessage")
#         message = event["message"]
#         username = event["username"]
        
#         await self.send(text_data = json.dumps({'message':message, 'username':username}))     #dumps() = json object --to--> string of json type


