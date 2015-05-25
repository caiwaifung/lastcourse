import sys
import os

if len(sys.argv) != 4:
    print 'usage: python <me> <feature> <data> <dim>'
    print 'example: python run.py PCA4 data5k 4'
    sys.exit(1)

os.system('make clean')
os.system('make DIM={}'.format(sys.argv[3]))

d = '../data/feature-{}/{}.feature'.format(sys.argv[1], sys.argv[2])
q = '../data/feature-{}/query.feature'.format(sys.argv[1])
os.system("./a {} {} ../result/ans.txt".format(d, q))
