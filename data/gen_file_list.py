import os
import random

a = os.listdir('./image')
random.shuffle(a)

b=a[5000:]
a=a[:5000]

def genlist(flist, fname):
    ftest = open(fname, 'w')
    for k in flist:
        ftest.write(k + '\n')
    ftest.close()

genlist(b, 'query.txt')
genlist(a[:1000], 'data1k.txt')
genlist(a[:2000], 'data2k.txt')
genlist(a[:3000], 'data3k.txt')
genlist(a[:4000], 'data4k.txt')
genlist(a[:5000], 'data5k.txt')
