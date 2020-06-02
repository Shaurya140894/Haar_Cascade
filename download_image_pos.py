import urllib.request
import cv2
import numpy as np
import os

def store_raw_image_pos():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04200800'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 990

    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos/" + str(pic_num) + ".jpg")
            img = cv2.imread("pos/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


store_raw_image_pos()