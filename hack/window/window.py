import asyncio
import websockets
from .send_frames import send_frames

def window():
    try:
        server = websockets.serve(send_frames, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()
        try:
            server.wait_closed() 
        except KeyboardInterrupt:
            pass
    except KeyboardInterrupt:
        print('exit')