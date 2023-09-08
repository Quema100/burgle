import cv2 as cv

def webcam():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            #dst = cv.resize(frame, dsize=(640, 480), interpolation=cv.INTER_AREA)
            # Our operations on the frame come here
            #gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv.imshow('Webcam',frame)

            if cv.waitKey(1)  & 0xFF == ord('q'):
                print('Exit')
                break

            if cv.getWindowProperty('Webcam', cv.WND_PROP_VISIBLE) <1:
                print('Exit')
                break

        except KeyboardInterrupt:
            print('Exit')
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()