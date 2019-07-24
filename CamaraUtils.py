import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while (True):
    # capture frame-by-frame
    ret, frame = cap.read()

    # our operation on the frame come here
    show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # display the resulting frame
    cv2.imshow('frame', show)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
        break
# when everything done , release the capture
cap.release()
cv2.destroyAllWindows()