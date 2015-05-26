import os
import numpy as np
import cv2

for s in ['data1k', 'data2k', 'data3k', 'data4k', 'data5k', 'query']:
        f1 = open('feature-PCA16/' + s + '.feature', 'r')
        f2 = open('feature-ColorMomentHSV9/' + s + '.feature', 'r')
        g = open('feature-Composite25/' + s + '.feature', 'w')

        p = f1.readlines()
        q = f2.readlines()

        for i in range(len(p)):
                if i > 0:
                        qq = map(float, q[i].strip().split(' '))
                        for j in xrange(len(qq)):
                                qq[j] *= 0.11

                        #qs = q[i].strip()
                        qs = ''
                        for s in qq:
                                qs = qs + str(s) + ' '
                        
                        p[i] = p[i].strip() + ' ' + qs + '\n'
                        g.write(p[i])
                else:
                        g.write(str(len(p)-1) + ' 25\n')
        f1.close()
        f2.close()
        g.close()

