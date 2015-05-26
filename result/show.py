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
pairs = f.readlines()[1::2]
ans = [x.strip().split(' ')[::2] for x in pairs]
ans = [[int(i) for i in x] for x in ans]
f.close()

#f = open('ans0.txt', 'r')
#ans0 = [int(x.split(' ')[0]) for x in f.readlines()]
#f.close()

f = open('a.html', 'w')
print >>f, '<!DOCTYPE html>'
print >>f, '<html> <body>'
print >>f, '<table>'
print >>f, '<tr>'
print >>f, '<td align="center">Query</td>'
print >>f, '<td align="center"></td>'
print >>f, '<td align="center">1st Closest</td>'
print >>f, '<td align="center">2nd Closest</td>'
print >>f, '<td align="center">3rd Closest</td>'
print >>f, '<td align="center">4th Closest</td>'
print >>f, '<td align="center">5th Closest</td>'
print >>f, '</tr>'
for i in range(min(100, len(ans))):
    std = b[i].split('_')[0]
    td = '<td align="center">'
    template = 'alt="" style="height:50px;max-width:70px" align="center"'
    print >>f, '<tr>'
    print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, b[i], template)
    print >>f, '<td width="10"></td>'
    for k in ans[i]:
        ok_icon = '<img src="ok-icon.png" alt="" style="height:15px;width:15px">' 
        flag = ok_icon if a[k].split('_')[0] == std else ''
        print >>f, '{}<img src="../data/image/{}" {}>'.format(td, a[k], template)
        print >>f, '{}</td>'.format(flag)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()
