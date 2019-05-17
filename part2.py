import numpy as np
import time
import cv2
from PIL import ImageGrab

print('jai mata di lets rock')
last_time = time.time()
while(1):
    last_time = time.time()
    img = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)
    rect = (200,150,400,160)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    cv2.imshow('window', img)
    print('{} seconds'.format(time.time()-last_time))
    if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
