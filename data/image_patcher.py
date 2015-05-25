import os
import numpy
import cv2
import math

def real_vec_normalize(v):
        n = len(v)
        m = sum(v) * 1. / n
        sv = 0.
        for i in xrange(n):
                v[i] = v[i] - m
                sv = sv + v[i] * v[i]
        if sv == 0:
                return

        sv = 1. / math.sqrt(sv)
        
        for i in xrange(n):
                v[i] = v[i] * sv

def patch_image_file(fname):
        inf = 'image/' + fname + '.JPEG'
        im = cv2.imread(inf)
        
        h = im.shape[0]
        w = im.shape[1]
        ff = min(32. / h, 32. / w)
        im = cv2.resize(im, (0,0), fx = ff, fy = ff)
        
        ouf = 'KMeans/' + fname + '.txt'
        
        h = im.shape[0]
        w = im.shape[1]

        P = 4
        f = open(ouf, 'w')
        for i in xrange(h-P):
                for j in xrange(w-P):
                        pat = []
                        for x in xrange(P):
                                for y in xrange(P):
                                        pat.append(im[i,j,0])
                                        pat.append(im[i,j,1])
                                        pat.append(im[i,j,2])
                        first = True
                        real_vec_normalize(pat)
                        for pa in pat:
                                f.write(('' if first else ' ') + str(pa))
                                first = False

                        f.write('\n')
        f.close()

a = os.listdir('./image')
for s in a:
        patch_image_file(s[:-5])

# Use matlab to compute K-Means centroids for K in 4, 8, 12 ... 24
# See runkmeans.m
