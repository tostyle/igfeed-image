import face_detect.image as img_util
import cv2
import os

def test ():
  print("restttt")

def detect_and_save_face(id, img):
  current_path = os.getcwd()
  cascPath = "haarcascade_frontalface_default.xml"
  faceCascade = cv2.CascadeClassifier(cascPath)
  print("faceCascade", faceCascade, cascPath)
  faces = faceCascade.detectMultiScale(
        img,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )
  for (x, y, w, h) in faces:
    img_util.save_img(id, img[y:y+h,x:x+w])
  return faces