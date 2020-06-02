import urllib.request
import cv2
import numpy as np
import os

def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir('uglies'):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread(current_image_path)
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print("Deletng this pic")
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


find_uglies()
