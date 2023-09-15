import asyncio
import websockets
from .send_voice import send_voice

def voice():
    try:
        server = websockets.serve(send_voice, "localhost", 8767)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print('exit')
