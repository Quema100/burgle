import asyncio
import websockets
import queue
import sounddevice as sd
import numpy as np

volume_multiplier = 10.0  # 볼륨을 조절하기 위한 스칼라 값
sample_rate = 88200  # 샘플 속도 설정 (예: 44100 Hz)
block_size = 16384  # 오디오 블록 크기

def clip_audio(data, factor=1.0):
    data[np.isnan(data)] = 0.0
    data[np.isinf(data)] = 0.0
    return np.clip(data * factor, -1.0, 1.0)

def input_audio_callback(indata, frames, time, status, queue):
    if status:
        print(status, flush=True)

    # 입력 데이터 처리
    outdata = clip_audio(indata, volume_multiplier)

    # 처리된 데이터를 출력 큐에 추가
    queue.put(outdata.copy())

def output_audio_callback(outdata, frames, time, status, queue,out_queue):
    #queue_size = queue.qsize()
    #print(f"큐에는 현재 {queue_size}개의 데이터가 있습니다.")
    if status:
        print(status, flush=True)

    # 출력 큐에서 데이터 가져오기
    if not queue.empty():
        out_queue.put(outdata)
    else:
        outdata.fill(0.0)

def start_stream(queue,out_queue):

    sample_rate = 88200  # 샘플 속도 설정 (예: 44100 Hz)
    input_stream = sd.InputStream(callback=lambda indata, frames, time, status: input_audio_callback(indata, frames, time, status, queue),
                                  channels=2, samplerate=sample_rate, blocksize=32768)
    output_stream = sd.OutputStream(callback=lambda outdata, frames, time, status: output_audio_callback(outdata, frames, time, status, queue,out_queue),
                                    channels=2, samplerate=sample_rate, blocksize=16384)

    # 입력 스트림 및 출력 스트림 시작
    input_stream.start()
    output_stream.start()

    return input_stream, output_stream

async def send_voice(websocket, path):
    out_queue = queue.Queue()
    start_queue = queue.Queue()
    input_stream, output_stream = start_stream(start_queue,out_queue)
    try:
        while True: 
            mix = out_queue.get()
            if not start_queue.empty():
                output_data = start_queue.get()
                extracted_data = mix[:len(output_data)].copy() 
                extracted_data = output_data               
                data = extracted_data.tobytes()                    
                await websocket.send(data)  # 데이터 전송
            else:
                mix.fill(0.0)
    except Exception as e:
        print(f"Voice Error: {str(e)}")
        await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Connection closed")
        await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosedOK:
        pass
