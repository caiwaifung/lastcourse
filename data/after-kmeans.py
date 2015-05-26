import os
import numpy as np
import cv2
import math

def dlmread(s, sp=' '):
        f = open(s, 'r')
        p = f.readlines()
        for i in range(len(p)):
                p[i] = map(float,p[i].split(sp))
        return np.array(p)
        


f = open('data5k.txt', 'r')
a = f.readlines()#os.listdir('./image-normalized')
f.close()
f = open('query.txt', 'r')
a = a + f.readlines()
f.close()
n = len(a)

r4 = np.zeros([n,4])
r8 = np.zeros([n,8])
r12 = np.zeros([n,12])
r16 = np.zeros([n,16])
r20 = np.zeros([n,20])
r24 = np.zeros([n,24])

k4 = dlmread('kmeans4.txt',',')
k8 = dlmread('kmeans8.txt',',')
k12 = dlmread('kmeans12.txt',',')
k16 = dlmread('kmeans16.txt',',')
k20 = dlmread('kmeans20.txt',',')
k24 = dlmread('kmeans24.txt',',')

def dist(z):
        return max(0, 1. / (0.2 + z) - 0.4)

index = 0
for s in a:
        fname = s[:-5]
        g = dlmread('KMeans/' + fname + 'txt')
        print(g.shape)
        
        h = g.shape[0]
        for i in range(h):
                for j in range(4):
                        z = g[i] - k4[j]
                        r4[index, j] += dist(np.dot(z, z))
                for j in range(8):
                        z = g[i] - k8[j]
                        r8[index, j] += dist(1+np.dot(z, z))
                for j in range(12):
                        z = g[i] - k12[j]
                        r12[index, j] += dist(1+np.dot(z, z))
                for j in range(16):
                        z = g[i] - k16[j]
                        r16[index, j] += dist(1+np.dot(z, z))
                for j in range(20):
                        z = g[i] - k20[j]
                        r20[index, j] += dist(1+np.dot(z, z))
                for j in range(24):
                        z = g[i] - k24[j]
                        r24[index, j] += dist(1+np.dot(z, z))
                        
        for j in range(4):
                r4[index, j] /= h
        for j in range(8):
                r8[index, j] /= h
        for j in range(12):
                r12[index, j] /= h
        for j in range(16):
                r16[index, j] /= h
        for j in range(20):
                r20[index, j] /= h
        for j in range(24):
                r24[index, j] /= h

        index = index + 1

for i in [4, 8, 12, 16, 20, 24]:
        for s in ['data1k', 'data2k', 'data3k', 'data4k', 'data5k', 'query']:
                f = open(s + '.txt', 'r')
                g = open('feature-KMeans' + str(i) + '/' + s + '.feature', 'w')
                rr = f.readlines()
                lr = len(rr)
                g.write(str(lr) + ' ' + str(i) + '\n')
                j = 0
                if lr == 613:
                        j = 5000
                r = r4
                if i==8:
                        r = r8
                if i==12:
                        r = r12
                if i==16:
                        r = r16
                if i==20:
                        r = r20
                if i==24:
                        r = r24
                for k in xrange(lr):
                        for ft in r[j,:]:
                                g.write(str(ft) + ' ')
                        g.write('\n')
                        j = j + 1
                f.close()
                g.close()
