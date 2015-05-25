import os
import numpy
import cv2

def normalize_image(img):
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
        img = cv2.resize(img, (32,32))
        return img

def normalize_image_file(fname):
        inf = 'image/' + fname + '.JPEG'
        ouf = 'image-normalized/' + fname + '.png'
        im = cv2.imread(inf)
        om = normalize_image(im)
        cv2.imwrite(ouf, om)


a = os.listdir('./image')
for s in a:
        normalize_image_file(s[:-5])
