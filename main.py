from multiprocessing import Process
from hack import window, webcam , voice

def main():
    try:
        # 프로세스 생성
        window_process = Process(target=window.window)
        webcam_process = Process(target=webcam.webcam)

        # 각 프로세스 시작
        window_process.start()
        webcam_process.start()

        # 각 프로세스 종료 대기
        window_process.join()
        webcam_process.join()

        print('hello, world!')
    except KeyboardInterrupt:
        print('Exit')

if __name__ == '__main__':
    main()