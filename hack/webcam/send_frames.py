import websockets
import cv2
import sys

async def send_frames(websocket, path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            _, buffer = cv2.imencode('.png', frame)
            png_data = buffer.tobytes()

            await websocket.send(png_data)

    except Exception as e:
        print(f"Webcam Error: {str(e)}")
    except KeyboardInterrupt:
        print("Connection closed")
        cap.release()
        sys.exit(0)
    except websockets.exceptions.ConnectionClosedOK:
        pass 
