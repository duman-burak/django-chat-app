import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope['user']
        type_control = text_data_json['type_control']
        m=Message.objects.create(content=message,user=user,room_id=self.room_name,type_control=type_control)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message",
                "message": message,
                'user' : user.username,
                'date' : m.get_short_date(),
                'type_control' : type_control,
                }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event['user']
        date = event['date']
        type_control = event['type_control']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            'user':user,
            'date':date,
            'type_control' : type_control,
            }))