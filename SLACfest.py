import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D

print('dude is this on')

def plot(img):
    cv2.line(img, (400,0), (400,640), 255)
    cv2.line(img, (200,0), (200,640), 255)
    cv2.line(img, (600,0), (600,640), 255)
    cv2.line(img, (0,320), (800,320), 255)
    cv2.line(img, (0,160), (800,160), 255)
    cv2.line(img, (0,480), (800,480), 255)

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    return cv2.bitwise_and(img, mask)

def process_img(original_image):
    processed_img = cv2.Canny(cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY), threshold1=200, threshold2=300)
    vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
    processed_img = roi(cv2.GaussianBlur(processed_img,(5,5),0), [vertices])
    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    plot(processed_img)
    return processed_img

def main():
    last_time = time.time()
    while(True):
        screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,40, 800, 640))),cv2.COLOR_BGR2RGB)
        new_screen = process_img(screen)
        print('{} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)

        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([10,100,100])
        upper_yellow = np.array([30,255,255])
    
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(screen,screen, mask= mask)

        cv2.imshow('frame',screen)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()
