import time
from PIL import ImageGrab
import cv2
import numpy as np
screen = np.array(cv2.imread('grab.png',cv2.IMREAD_COLOR))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(screen, cv2.COLOR_RGB2HSV)
lower_yellow = np.array([60, 100, 60])
higher_yellow = np.array([60, 40, 60])
mask = cv2.inRange(hsv, lower_yellow, higher_yellow)
res = cv2.bitwise_and(screen, screen, mask= mask)
print(screen)
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
cv2.imshow('window', screen)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
