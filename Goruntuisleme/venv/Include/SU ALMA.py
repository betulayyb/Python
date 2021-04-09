import cv2
import numpy as np

lower_blue = np.array([90, 150, 100])
upper_blue = np.array([110, 255, 255])

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    kenarlar = cv2.Canny(frame, 100, 150)
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    griton = np.float32(griton)

    koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
    koseler = np.int0(koseler)

    for kose in koseler:
        x, y = kose.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('orjinal',frame)
    cv2.imshow('koseler', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('kenarlar', kenarlar)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

lower_blue = np.array([90, 150, 100])
upper_blue = np.array([110, 255, 255])

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    kenarlar = cv2.Canny(frame, 100, 150)
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    griton = np.float32(griton)

    koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
    koseler = np.int0(koseler)

    for kose in koseler:
        x, y = kose.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('orjinal',frame)
    cv2.imshow('koseler', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('kenarlar', kenarlar)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

lower_blue = np.array([90, 150, 100])
upper_blue = np.array([110, 255, 255])

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    kenarlar = cv2.Canny(frame, 100, 150)
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    griton = np.float32(griton)

    koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
    koseler = np.int0(koseler)

    for kose in koseler:
        x, y = kose.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('orjinal',frame)
    cv2.imshow('koseler', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('kenarlar', kenarlar)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

lower_blue = np.array([90, 150, 100])
upper_blue = np.array([110, 255, 255])

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    kenarlar = cv2.Canny(frame, 100, 150)
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    griton = np.float32(griton)

    koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
    koseler = np.int0(koseler)

    for kose in koseler:
        x, y = kose.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('orjinal',frame)
    cv2.imshow('koseler', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('kenarlar', kenarlar)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

lower_blue = np.array([90, 150, 100])
upper_blue = np.array([110, 255, 255])

kamera=cv2.VideoCapture(0)

while(1):
    ret,frame=kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    kenarlar = cv2.Canny(frame, 100, 150)
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    griton = np.float32(griton)

    koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
    koseler = np.int0(koseler)

    for kose in koseler:
        x, y = kose.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow('orjinal',frame)
    cv2.imshow('koseler', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('kenarlar', kenarlar)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
