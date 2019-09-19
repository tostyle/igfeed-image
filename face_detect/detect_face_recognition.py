import face_recognition
import cv2
import os
import face_detect.image as img_util

def detect_and_save_face(id, img):
  face_locations = face_recognition.face_locations(img)
  for (top, right, bottom, left) in face_locations:
    img_util.save_img(id, img[top:bottom, left:right])
  return face_locations