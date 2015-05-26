import sys
import os

if len(sys.argv) != 4:
    print 'usage: python <me> <feature> <data> <dim>'
    print 'example: python run.py PCA4 data5k 4'
    sys.exit(1)

os.system('mingw32-make clean')
os.system('mingw32-make DIM={}'.format(sys.argv[3]))

d = '../data/feature-{}/{}.feature'.format(sys.argv[1], sys.argv[2])
q = '../data/feature-{}/query.feature'.format(sys.argv[1])
ret = os.system("a.exe {} {} ../result/ans.txt".format(d, q))
sys.exit(ret)
