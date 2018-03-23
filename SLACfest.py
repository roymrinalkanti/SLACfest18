import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D

print('dude is this on')

def main(): 
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    last_time = time.time()
    while(True):
        #PressKey(W)
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,600)))
        #print('{} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.Canny(cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY), threshold1= 200, threshold2=300))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('done')
            cv2.destroyAllWindows()
            break

main()
