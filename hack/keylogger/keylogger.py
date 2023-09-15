import asyncio
import websockets
from log import log

def keylogger():
    try:
        server = websockets.serve(send_voice, "localhost", 8768)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()
        try:
            server.wait_closed() 
        except KeyboardInterrupt:
            pass    
    except KeyboardInterrupt:
        print('exit')

if __name__ == '__main__':
    keylogger()