from tkinter.tix import IMAGE
import cv2
import uuid
import os
import time

""" Image taking and labeling """

labels = ['teodiopedro','uwu','demonio','nice']
num_images = 5 # How many images are been taking for each label
IMAGES_PATH = os.path.join('tensorflow','workspace','images')

if not os.path.exists(IMAGES_PATH):
   os.makedirs(IMAGES_PATH)
   
# Create label folders
for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(label_path):
        os.mkdir(label_path)

