import asyncio
import websockets
from .send_frames import send_frames

def webcam():
    try:
        server = websockets.serve(send_frames, "localhost", 8766)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print('exit')