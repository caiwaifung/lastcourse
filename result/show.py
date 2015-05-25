#from PIL import Image
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

f = open('ans0.txt', 'r')
ans0 = [int(x.split(' ')[0]) for x in f.readlines()]
f.close()

f = open('a.html', 'w')
print >>f, '<!DOCTYPE html>'
print >>f, '<html> <body>'
print >>f, '<table>'
for i in range(min(100, len(ans))):
    x = b[i].split('_')[0]
    y = a[ans[i]].split('_')[0]
    z = a[ans0[i]].split('_')[0]
    l1 = 'Yes' if x == y else ''
    l2 = 'Yes' if x == z else ''

    template = 'alt="a0" style="height:100px;max-width:160px" align="center"'
    print >>f, '<tr>'
    print >>f, '<td><img src="../data/image/{}" {}></td>'.format(b[i], template)
    print >>f, '<td><img src="../data/image/{}" {}></td>'.format(a[ans[i]], template)
    print >>f, '<td>{}</td>'.format(l1)
    print >>f, '<td><img src="../data/image/{}" {}></td>'.format(a[ans0[i]], template)
    print >>f, '<td>{}</td>'.format(l2)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()

c1 = c2 = 0

for i in range(min(900, len(ans))):
    x = b[i].split('_')[0]
    y = a[ans[i]].split('_')[0]
    z = a[ans0[i]].split('_')[0]
    if x == y:
        c1 += 1
    if x == z:
        c2 += 1

print len(ans), c1, c2
