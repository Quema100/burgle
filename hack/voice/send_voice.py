import asyncio
import sys
import websockets
import pyaudio
import numpy as np

FORMAT = pyaudio.paFloat32
CHANNELS = 2
RATE = 88200
CHUNK = 259072
AMPLIFICATION_FACTOR = 5.0  

async def send_voice(websocket, path):

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Streaming and playing audio...")

    try:
        while True:
            data = stream.read(CHUNK)

            audio_data = np.frombuffer(data, dtype=np.float32)

            amplified_audio_data = np.clip(audio_data * AMPLIFICATION_FACTOR, -1.0, 1.0)

            amplified_data = amplified_audio_data.tobytes()

            await websocket.send(amplified_data) 
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Finished streaming")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        sys.exit(0)
        pass
    except asyncio.CancelledError:
        pass
    except websockets.exceptions.ConnectionClosedOK:
        pass