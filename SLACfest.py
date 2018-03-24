import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D

print('dude is this on')

def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
            print(lines)
    except:
        pass

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
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    #draw_lines(processed_img,lines)
    plot(processed_img)
    return processed_img

def main():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
        new_screen = process_img(screen)
        print('{} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
