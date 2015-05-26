import sys
import os

if len(sys.argv) != 5:
    print 'usage: python <me> <prog> <feature> <data> <dim>'
    print 'example: python run.py vio PCA4 data5k 4'
    sys.exit(1)
prog = sys.argv[1]
feature = sys.argv[2]
data = sys.argv[3]
dim = sys.argv[4]

source = '{}.cpp'.format(prog)
target = prog
flags = '-DFEATURE_DIM={} -Wall -Wconversion -Wextra --std=c++11'.format(dim)

print '|run.py| Compiling...'
ret = os.system('g++ {} -o {} {}'.format(source, target, flags))
if ret != 0:
    print 'failed to compile. EXITCODE={}'.format(ret)
    sys.exit(ret)

print
print '|run.py| Running...'
d = '../data/feature-{}/{}.feature'.format(feature, data)
q = '../data/feature-{}/query.feature'.format(feature)
ret = os.system("./{} {} {} ../result/ans.txt".format(target, d, q))
if ret != 0:
    print 'failed to run. EXITCODE={}'.format(ret)
    sys.exit(ret)

print
print '|run.py| Printing Stat...'
os.chdir('../result')
os.system('python show.py {}'.format(data))
os.system('python stat.py {}'.format(data))
