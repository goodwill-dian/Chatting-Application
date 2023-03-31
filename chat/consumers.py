from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MyAsyncConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("Inside Connect")
        # self.roomGroupName = 'chat-group'
        # await self.channel_layer.group_add(
        #     self.roomGroupName,
        #     self.channel_name
        # )
        
        await self.accept()
        
    async def disconnect(self, close_code):
        print("Inside Disconnect")
        # await self.channel_layer.group_discard(
        #     self.roomGroupName,
        #     self.channel_layer
        # )
        raise StopConsumer()
        
    async def receive(self, text_data):
        print("Inside Receive")
        text_data_json = json.loads(text_data)                                  #loads() = string --to--> json
        
        message = text_data_json['message']
        username = text_data_json['username']
        
        await self.send(text_data = json.dumps({'message':message, 'username':username}))
        # await self.channel_layer.group_send(
        #     self.roomGroupName,{
        #         'type' : 'sendMessage',
        #         "message" : message,
        #         'username' : username,
        #     }
        # )
        
    # async def sendMessage(self, event):
    #     print("Inside sendMessage")
    #     message = event["message"]
    #     username = event["username"]
        
    #     await self.send(text_data = json.dumps({'message':message, 'username':username}))             #dumps() = json --to--> string






# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         await self.send({                           #Server accepts connection
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self, event):
#         print("Message from Front-End (Client) to Server is ->", event['text'])
#         await self.send({
#             'type':'websocket.send',
#             'text':'Message from Server to Front-End (Client)',
#         })

#     async def websocket_disconnect(self, event):
#         print("Async Disconnect -->", event)
#         raise StopConsumer()

