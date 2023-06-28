#1
import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n Insert FaceID <1-10> ==> ')

print ('\n Set up camera ...')
count = 0   #number of faces data (30 faces for 1 object)

while (True):
    ret, img = cam.read()
    #img = cv2.flip(img,-1)  #flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to gray scale
    faces = face_detector.detectMultiScale (gray,1.3,5)  #detect face

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)   #bounding box
        count +=1
        cv2.imwrite("dataset/User." + str(face_id) + "." + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow("Image", img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:
        break

print('\n[INFO] Exit')
cam.release()
cv2.destroyAllWindows()






