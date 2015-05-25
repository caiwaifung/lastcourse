from PIL import Image
import sys
import os

if len(sys.argv) != 2:
    print 'usage: python <me> <d>'
    print '  input: ../data/<d>.txt'
    print '  input: ../data/query.txt'
    print '  input: ans.txt'
    print 'the program then compare answers in query.txt and results in ans.txt'
    sys.exit(1)

f = open('../data/{}.txt'.format(sys.argv[1]), 'r')
a = [x.strip() for x in f.readlines()]
f.close()

f = open('../data/query.txt', 'r')
b = [x.strip() for x in f.readlines()]
f.close()

f = open('ans.txt', 'r')
ans = [int(x.split(' ')[0]) for x in f.readlines()]
f.close()

f = open('a.html', 'w')
print >>f, '<!DOCTYPE html>'
print >>f, '<html> <body>'
print >>f, '<table>'
for i in range(min(100, len(ans))):
    template = 'alt="a0" style="height:100px"'
    print >>f, '<tr>'
    print >>f, '<td><img src="../data/image/{}" {}></td>'.format(b[i], template)
    print >>f, '<td><img src="../data/image/{}" {}></td>'.format(a[ans[i]], template)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()
