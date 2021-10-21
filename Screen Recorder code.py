import cv2
import pyautogui as p
import numpy as np

rs= p.size()

fn= input("enter path")
fps= 60.0

fourcc= cv2.VideoWriter_fourcc(*"XVID") 
output= cv2.VideoWriter(fn, fourcc, fps, rs)

cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording", (720, 450))

while True:
    img= p.screenshot()
    f= np.array(img)
    f= cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live_Recording", f)
    k= cv2.waitKey(1)
    if k==ord("z") & 0xFF:
        break
        
#vid.release()
output.release()
cv2.destroyAllWindows()