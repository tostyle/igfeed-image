import pika
import json
import urllib.request
import numpy as np
import cv2
import os

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
current_path = os.getcwd()

def callback(ch, method, properties, body):
    feed_data = json.loads(body)
    print(" [x] Received %r" % feed_data['Link'])
    req = urllib.request.urlopen(feed_data['Link'])
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)  # 'Load it as it is'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
      print(x,y,w,h)
      # num = num+1
      # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
      cv2.imwrite(current_path +"/dataset/"+feed_data['ID']+".jpg", gray[y:y+h,x:x+w])
    # print(type(img))
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
