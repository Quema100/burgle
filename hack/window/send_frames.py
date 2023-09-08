from PIL import ImageGrab
import asyncio
import websockets
import cv2
import numpy as np

async def send_frames(websocket, path):
    while True:
        try:
            screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
            screenshot = cv2.resize(screenshot, (1520, 710))

            
            _, buffer = cv2.imencode('.png', screenshot)
            png_data = buffer.tobytes()

            await websocket.send(png_data)
        except Exception as e:
            print(f"Error: {str(e)}")
            break
        except KeyboardInterrupt:
            print("Connection closed")
            break
        except websockets.exceptions.ConnectionClosedOK:
            pass 