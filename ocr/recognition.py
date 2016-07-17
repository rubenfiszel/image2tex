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

    for cnt in contours:
        [x,y,w,h] = cv2.boundingRect(cnt)

        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,123), 4)
        roi = gray[y:y+h,x:x+w]
        #    roismall = cv2.resize(roi,(10,10))

    cv2.imshow('norm',im)
    key = cv2.waitKey(0)
    np.savetxt('symbol.data',samples)


def main():
    read_img('example_text.png')

if __name__ == "__main__":
    main()
