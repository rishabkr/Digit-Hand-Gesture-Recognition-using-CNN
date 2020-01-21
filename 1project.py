#TO-DO:
# Two rectangles
# Prediction
# Text to speech
# Model train
#Import libraries
from keras.models import load_model
import cv2
import copy
import numpy as np
#from gtts import gTTS
import os
import urllib.request

#Global Variables
rect1_tlx = None
rect1_tly = None
rect1_brx = None
rect1_bry = None
rect2_tlx = None
rect2_tly = None
rect2_brx = None
rect2_bry = None
numbers = [0,1,2,3,4,5]

def draw_rect(frame):
    rows,cols,_ = frame.shape
    global rect1_tlx,rect1_tly,rect1_brx,rect1_bry,rect2_tlx,rect2_tly,rect2_brx,rect2_bry
    #Rectangle one
#    rect1_tlx = int(1*cols/20)
#    rect1_brx = int(7*cols/20)
 #   rect1_tly = int(2*rows/20)
  #  rect1_bry = int(14*rows/20)
    #Rectangle two
   # rect2_tlx = int(13*cols/20)
    #rect2_brx = int(19*cols/20)
    #rect2_tly = int(2*rows/20)
    #rect2_bry = int(14*rows/20)

    cv2.rectangle(frame,(400,80),(600,280),(255,0,0),1)
    cv2.rectangle(frame,(20,80),(220,280),(255,0,0),1)

    return frame

def preprocess(roi):
    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roi = cv2.GaussianBlur(roi,(7,7),3)
    roi = cv2.adaptiveThreshold(roi,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret,roi_new = cv2.threshold(roi,25,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return roi_new

if __name__ == "__main__":

    model = load_model('../Required_data/model_6cat.h5')
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        _, window = capture.read()
        window = cv2.flip(window,1)
        frame = copy.deepcopy(window)
        frame = draw_rect(frame)
        roi1 = frame[80:280,400:600]
        roi2 = frame[80:280,20:220]
        roi1 = preprocess(roi1)
        roi1 = cv2.resize(roi1,(300,300))
     #   cv2.imshow("roi1",roi1)           ##DISPLAY1
        roi2 = preprocess(roi2)
        roi2 = cv2.resize(roi2,(300,300))
       # cv2.imshow("roi2",roi2)          ##DISPLAY2
        img1 = np.float32(roi1)/255.
        img1 = np.expand_dims(img1,axis=0)
        img1 = np.expand_dims(img1,axis=-1)
        img2 = np.float32(roi2)/255.
        img2 = np.expand_dims(img2,axis=0)
        img2 = np.expand_dims(img2,axis=-1)
        pred1 = numbers[np.argmax(model.predict(img1)[0])]
        pred2 = numbers[np.argmax(model.predict(img2)[0])]
        cv2.putText(frame,'Count: '+str(pred1+pred2),(10,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow("Live Feed",frame)     ##DISPLAY LIVE FEED
        pressed_key = cv2.waitKey(1)
        if pressed_key == 27:
            break
    cv2.destroyAllWindows()
    capture.release()
