import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # layer is to be created
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name!s}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        json_data = json.loads(text_data)
        message = json_data["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"message": message, "type": "send_back"}
        )

    def send_back(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
