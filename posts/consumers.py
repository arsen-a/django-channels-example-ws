from channels.generic.websocket import AsyncWebsocketConsumer


class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("posts", self.channel_name)
        await self.accept()

    async def new_post(self, event):
        await self.send(event['data'])
