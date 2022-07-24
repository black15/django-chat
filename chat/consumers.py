import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from account.models import Account
from chat.models import Message, Room

class ChatConsumer(AsyncWebsocketConsumer):
        async def connect(self):
                self.room_name          = self.scope['url_route']['kwargs']['room_name']
                self.room_group_name    = 'chat_%s' % self.room_name

                await self.channel_layer.group_add(
                        self.room_group_name,
                        self.channel_name
                )

                await self.accept()

        async def disconnect(self, code):
                await self.channel_layer.group_discard(
                        self.room_group_name,
                        self.channel_name
                )

        async def receive(self, text_data):
                data = json.loads(text_data)
                username        = data['username']
                room            = data['room']
                message         = data['message']

                await self.save_message(username, room, message)

                await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                                'type'          : 'chat_message',
                                'username'      : username,
                                'room'          : room,
                                'message'       : message,

                        }
                )

        async def chat_message(self, event):
                username        = event['username']
                room            = event['room']
                message         = event['message']

                await self.send(text_data=json.dumps({
                        'username'      : username,
                        'room'          : room,
                        'message'       : message,
                }))

        @sync_to_async
        def save_message(self, username, room, message):
                user = Account.objects.get(username=username)
                room = Room.objects.get(slug=room)

                Message.objects.create(
                        user    = user,
                        room    = room,
                        message = message,
                )