#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#final with text to speech
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pyttsx3
import threading

def convert_to_speech(labels):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute) as needed

    for label in labels:
        engine.say(label)

    engine.runAndWait()

def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture('http://192.168.43.239:81/stream')  # VideoCapture(0) for the default camera, or provide the index of the camera if multiple are available

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        bbox, label, conf = cv.detect_common_objects(frame)
        output_image = draw_bbox(frame, bbox, label, conf)

        # Extract the labels of recognized objects
        labels = [obj_label for obj_label in label]

        cv2.imshow("live transmission", output_image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        # Convert the labels to speech
        convert_to_speech(labels)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("started")
    t1 = threading.Thread(target=run1)
    t1.start()
    t1.join()

