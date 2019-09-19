import pika
import json
import urllib.request
import numpy as np
import cv2
import os
import face_detect.image as img_util
# import face_detect.detect_cascade as detect
import face_detect.detect_face_recognition as detect

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
current_path = os.getcwd()

def callback(ch, method, properties, body):
    feed_data = json.loads(body)
    print(" [x] Received %r" % feed_data['Link'])
    img = img_util.load_image_from_url(feed_data['Link'])
    format_img = img_util.format_img(img)
    faces = detect.detect_and_save_face(feed_data['ID'], format_img)
    print("Found {0} faces!".format(len(faces)))
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.imshow(feed_data['ID'], img)
    # if cv2.waitKey() & 0xff == 27: quit()

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_consume(
        queue='igfeed_pic',
        auto_ack=False,
        on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
