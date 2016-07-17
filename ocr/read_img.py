import numpy as np
import cv2

def read_img(filename):
    im = cv2.imread(filename)
    im3 = im.copy()

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

    #################      Now finding Contours         ###################

    _, contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    samples =  np.empty((0,100))
    im_list = []
    space_list = []
    for cnt in contours:
        [x,y,w,h] = cv2.boundingRect(cnt)
        space = (x+w/2, y+h/2, w, h)
        roi = gray[y:y+h,x:x+w]
        im_list.append(roi)
        space_list.append(space)
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255), 2)

    return (im_list, space_list)
