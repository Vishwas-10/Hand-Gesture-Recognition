import cv2
import os
import time
import numpy as np

def collectGestureImages():
    '''
    For collecting data we have created data folder with contain 2 sub folders
    test and train which contains 7 folders(1, 2, 3, 4, 5, YES, NO) each.
    '''
    # Setting a mode
    mode = 'Test'
    path = 'data/'+mode+'/' # Specifying the path where the image will be saved

    cam = cv2.VideoCapture(0) # Capturing the webcam stream
    time.sleep(1)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        # Simulating mirror image
        frame = cv2.flip(frame, 1) # Flipping the image

        # Getting count of existing images
        count = {'YES': len(os.listdir(path + "YES")),
                 'NO': len(os.listdir(path + "NO")),
                 '0': len(os.listdir(path + "/0")),
                 '1': len(os.listdir(path + "/1")),
                 '2': len(os.listdir(path + "/2")),
                 '3': len(os.listdir(path + "/3")),
                 '4': len(os.listdir(path + "/4")),
                 '5': len(os.listdir(path + "/5"))}

        # Printing the count in each set to the screen
        cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "IMAGE COUNT : ", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "YES : " + str(count['YES']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "NO : " + str(count['NO']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "ZERO : " + str(count['0']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "ONE : " + str(count['1']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "TWO : " + str(count['2']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "THREE : " + str(count['3']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "FOUR : " + str(count['4']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        cv2.putText(frame, "FIVE : " + str(count['5']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

        # Setting up Coordinates of the Region of interest (ROI)
        x1,y1 = int(0.5 * frame.shape[1]), 10
        x2,y2 = frame.shape[1] - 10, int(0.5 * frame.shape[1])

        # Showing ROI
        cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)

        # Extracting the ROI
        roi = frame[y1:y2, x1:x2]
        roi = cv2.resize(roi, (64, 64))

        cv2.imshow("Frame", frame)

        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Applying gaussian blur
        roi = cv2.GaussianBlur(roi, (5, 5), 0)

        # Thresholdin' Otsu's Binarization
        _, roi = cv2.threshold(roi, 107, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        cv2.imshow("ROI", roi)

        interrupt = cv2.waitKey(10)
        if interrupt & 0xFF == 27:  # esc key
            break
        if interrupt & 0xFF == ord('y'):
            cv2.imwrite(path + 'YES/' + str(count['YES']) + '.jpg', roi)
        if interrupt & 0xFF == ord('n'):
            cv2.imwrite(path + 'NO/' + str(count['NO']) + '.jpg', roi)
        if interrupt & 0xFF == ord('0'):
            cv2.imwrite(path + '0/' + str(count['0']) + '.jpg', roi)
        if interrupt & 0xFF == ord('1'):
            cv2.imwrite(path + '1/' + str(count['1']) + '.jpg', roi)
        if interrupt & 0xFF == ord('2'):
            cv2.imwrite(path + '2/' + str(count['2']) + '.jpg', roi)
        if interrupt & 0xFF == ord('3'):
            cv2.imwrite(path + '3/' + str(count['3']) + '.jpg', roi)
        if interrupt & 0xFF == ord('4'):
            cv2.imwrite(path + '4/' + str(count['4']) + '.jpg', roi)
        if interrupt & 0xFF == ord('5'):
            cv2.imwrite(path + '5/' + str(count['5']) + '.jpg', roi)
    cam.release()
    cv2.destroyAllWindows()
