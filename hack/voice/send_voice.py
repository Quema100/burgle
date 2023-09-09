import sounddevice as sd
import numpy as np
import asyncio
import websockets

# 오디오 설정
sample_rate = 88200  # 샘플링 레이트 (Hz)
channels = 2  # 1은 모노, 2는 스테레오
volume_multiplier = 10.0  # 볼륨을 조절하기 위한 스칼라 값

# 입력 데이터를 클리핑하는 함수
def clip_audio(data, factor=1.0):
    return np.clip(data * factor, -1.0, 1.0)

# 오디오 캡처 및 재생 콜백 함수
def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(f"Error: {status}")

    # 입력된 오디오 데이터를 클리핑하고 볼륨을 조절한 후 출력으로 보내어 실시간 재생
    modified_audio = clip_audio(indata, volume_multiplier)
    outdata[:] = modified_audio

async def send_voice(websocket, path):
    try:
        with sd.InputStream(channels=channels, samplerate=sample_rate,blocksize=16384):
            while True:
                audio_data = sd.rec(frames=1024, channels=channels, samplerate=sample_rate, dtype='float32', blocking=True)
                audio_data = clip_audio(audio_data, volume_multiplier)
                await websocket.send(audio_data.tobytes())  # 데이터 전송
    except Exception as e:
        print(f"Webcam Error: {str(e)}")
    except KeyboardInterrupt:
        pass
    except websockets.exceptions.ConnectionClosedOK:
        pass 