import os
import numpy as np
import cv2

a = os.listdir('./image-normalized')
n = len(a)
#n = 500
m = 1024

data = np.zeros([n, m], dtype="float")

i = 0
for s in a:
        p = cv2.imread('image-normalized/' + s, 0).reshape(m)
        data[i] = p
        i = i + 1
        if i == n:
                break

def arrayOfArrayToMatlabString(array):
    return '[' + "\n ".join(" ".join("%g" % val for val in line) for line in array) + ']'


print(data.shape)
print(data)

f = open('data.m', 'w')
f.write('a='+arrayOfArrayToMatlabString(data)+';')
f.close()

# Use matlab to compute the PCA of data, because OpenCV runs too slow. =_=#
# See pca.m
