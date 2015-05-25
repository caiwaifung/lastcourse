import os
import numpy as np
import cv2

f = open('data5k.txt')
a = f.readlines()#os.listdir('./image-normalized')
f.close()
f = open('query.txt')
a = a + f.readlines()
f.close()

n = len(a)
print n
#n = 500
m = 1024

data = np.zeros([n, m], dtype="float")

i = 0
for s in a:
        ss = 'image-normalized/' + s[:-5] + 'png'
        p = cv2.imread(ss, 0).reshape(m)
        data[i] = p
        i = i + 1
        if i == n:
                break

eig = np.zeros([m, m], dtype="float")

mean = np.mean(data, axis=0)

f = open('eig.txt')
for i in xrange(m):
        s = f.readline()
        eig[i] = np.array(map(float, s.split(',')))
f.close()
eig = eig.transpose()
print(eig.shape)
print(eig)

res = np.zeros([n, 24], dtype="float")

for i in xrange(n):
        vec = data[i] - mean;
        for j in xrange(24):
                res[i, j] = np.dot(eig[j + 1], vec)

for i in [4, 8, 12, 16, 20, 24]:
        for s in ['data1k', 'data2k', 'data3k', 'data4k', 'data5k', 'query']:
                f = open(s + '.txt', 'r')
                g = open('feature-PCA' + str(i) + '/' + s + '.feature', 'w')
                rr = f.readlines()
                print len(rr)
                
                g.write(str(len(rr)) + ' ' + str(i) + '\n')
                j = 0
                if s == 'query':
                    j = 5000
                for k in xrange(len(rr)):
                    for ft in res[j,:i]:
                        ff = np.sqrt(ft) if ft >= 0 else -np.sqrt(-ft)
                        g.write(str(ff) + ' ')
                    g.write('\n')
                    j = j + 1

                f.close()
                g.close()

es = np.zeros([m, m, 3], dtype="float")

for i in xrange(m):
        mn = -min(eig[i,:])
        mx = +max(eig[i,:])
        mm = 256 / max(mn, mx)

        for j in xrange(m):
                d = eig[i,j]*mm
                es[i,j,2] = 0 if d<0 else +d
                es[i,j,0] = 0 if d>0 else -d
                es[i,j,1] = 0 if d>0 else -d
em = []

for i in xrange(m):
        em.append(es[i].reshape(32,32,3))
        em[i] = cv2.resize(em[i], (256, 256))
        cv2.imwrite('PCA_visualize/eigvec' + str(i) + '.png', em[i])
