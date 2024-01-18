# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ComplaintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Handle the incoming data as needed
        data = json.loads(text_data)
        # Perform any necessary operations, e.g., updating the database
        # ...

        # Broadcast the updated data to all connected clients
        await self.send(text_data=json.dumps({
            'message': 'Data updated successfully',
        }))
