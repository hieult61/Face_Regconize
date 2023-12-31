#2
import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getImageAndLabel(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:  #Take ID and attach Label
        PIL_img = Image.open(imagePath).convert('L')  #convert to gray scale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples, ids

print ("\nTraning data ...")
faces,ids = getImageAndLabel(path)
recognizer.train(faces, np.array(ids))
recognizer.write("trainer/trainer.yml") #File used to recognize face
print ("\n {0} faces trained. Exit".format(len(np.unique(ids))))