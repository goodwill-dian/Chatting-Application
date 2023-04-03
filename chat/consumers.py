from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MyAsyncConsumer(AsyncWebsocketConsumer):
    
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
        text_data_json = json.loads(text_data)                                  #loads() = json --to--> string
        
        message = text_data_json['message']
        # username = text_data_json['username']
        
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message ,
                # "username" : username ,
            })
        
    async def sendMessage(self, event):
        print("inside sendmessage")
        message = event["message"]
        # username = event["username"]
        print(self.request.user.first_name)
        
        await self.send(text_data = json.dumps({'message':message, 'username':self.request.user.first_name}))             #dumps() = string --to--> json


