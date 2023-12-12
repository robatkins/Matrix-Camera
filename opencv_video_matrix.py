import cv2

RES = 1600, 900
main_capture = cv2.VideoCapture('video/video_file.mp4')
background_capture = cv2.VideoCapture('video/matrix.mkv')
subtractor = cv2.createBackgroundSubtractorKNN()

while True:
    frame = main_capture.read()[1]
    frame = cv2.resize(frame, RES, interpolation=cv2.INTER_AREA)
    mask = subtractor.apply(frame, 1)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('', bitwise)
    if cv2.waitKey(1) == 27:
        break