import numpy as np
from PIL import ImageGrab
import cv2
import time

print('dude is this on')

def main(): 
    last_time = time.time()
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,640,400)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.Canny(cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY), threshold1= 200, threshold2=300))
        if cv2.waitKey(5) & 0xFF == ord('q'):
            print('done')
            cv2.destroyAllWindows()
            break

main()
