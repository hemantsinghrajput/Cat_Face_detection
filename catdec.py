import cv2
import numpy as np
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\\Users\\a\\AppData\\Roaming\\Python\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalcatface.xml')

while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j)
    print(face)
    
    for (x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
       
    
    cv2.imshow('orignal img',i)

    k=cv2.waitKey(1)
    if(k==27):
        break
cv2.destroyAllWindows()
