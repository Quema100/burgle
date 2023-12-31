from PIL import ImageGrab
import websockets
import cv2
import numpy as np

async def send_frames(websocket, path):
    while True:
        try:
            screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
            
            _, buffer = cv2.imencode('.png', screenshot)
            png_data = buffer.tobytes()

            await websocket.send(png_data)
        except Exception as e:
            print(f"Window Error: {str(e)}")
            break
        except KeyboardInterrupt:
            print("Connection closed")
            break
        except websockets.exceptions.ConnectionClosedOK:
            pass 