import numpy as np
import cv2
from PIL import ImageGrab

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    frame = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
