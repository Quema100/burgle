from multiprocessing import Process
from hack import window, webcam , voice

def main():
    try:
        window_process = Process(target=window.window)
        webcam_process = Process(target=webcam.webcam)
        voice_process = Process(target=voice.voice)

        window_process.start()
        webcam_process.start()
        voice_process.start()

        window_process.join()
        webcam_process.join()
        voice_process.join()

    except KeyboardInterrupt:
        print('Exit')

if __name__ == '__main__':
    main()