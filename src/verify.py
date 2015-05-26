import numpy as np
import sys

if len(sys.argv) != 2:
    print 'usage: python <me> data_file'
    sys.exit(1)

f = open(sys.argv[1], 'r')
lines = f.readlines()[1:]
f.close()

print len(lines)
