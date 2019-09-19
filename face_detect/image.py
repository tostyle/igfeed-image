import urllib.request
import numpy as np
import cv2
import os

def load_image_from_url (url):
  req = urllib.request.urlopen(url)
  arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
  img = cv2.imdecode(arr, -1)
  return img

def format_img (img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return gray

def save_img(id, img):
  current_path = os.getcwd()
  print("current_path=", current_path,id ,img)
  cv2.imwrite(current_path +"/dataset/"+id+".jpg", img)