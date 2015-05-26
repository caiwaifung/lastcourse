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
ans = [x.split(' ')[1::2] for x in f.readlines()]
ans = [[int(i) for i in x] for x in ans]
f.close()

#f = open('ans0.txt', 'r')
#ans0 = [int(x.split(' ')[0]) for x in f.readlines()]
#f.close()

f = open('a.html', 'w')
print >>f, '<!DOCTYPE html>'
print >>f, '<html> <body>'
print >>f, '<table border="1">'
for i in range(min(100, len(ans))):
    std = b[i].split('_')[0]

    td = '<td align="center">'
    template = 'alt="a0" style="height:80px;max-width:110px" align="center"'
    print >>f, '<tr>'
    print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, b[i], template)
    print >>f, '<td width="50"></td>'
    for k in ans[i]:
        flag = 'Yes' if a[k].split('_')[0] == std else ''
        print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, a[k], template)
        print >>f, '{}{}</td>'.format(td, flag)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()
