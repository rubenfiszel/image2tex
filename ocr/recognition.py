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
    info_list = []
    for cnt in contours:
        [x,y,w,h] = cv2.boundingRect(cnt)
        space = (x+w/2, y+h/2, w, h)
        roi = gray[y:y+h,x:x+w]
        info_list.append((roi, space))
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255), 2)

    return info_list

def regulize(info_list):

    regulized_info_list = []

    for info in info_list:
        ninfo = info
        (roi, space) = ninfo
        cv2.imshow('norm', roi)
        cv2.waitKey()
        regulized_info_list.append(ninfo)

    return info_list


def main():
    info_list = read_img('example_text.png')
    regulized = regulize(info_list)

if __name__ == "__main__":
    main()
