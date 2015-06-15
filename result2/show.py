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

labels = ['',
    'n01613177', 'n01923025', 'n02278980', 'n03767203', 'n03877845',
    'n04515003', 'n04583620', 'n07897438', 'n10247358', 'n11669921']

f = open('../result/res.txt', 'r')
lines = f.readlines()
f.close()
res = [int(line.split(',')[0]) for line in lines]
res = [labels[i] for i in res]
ans = []
for label in res:
    cur = []
    for i in range(len(a)):
        if a[i].split('_')[0] == label:
            cur.append(i)
            if len(cur) >= 3:
                break
    ans.append(cur)

#f = open('ans0.txt', 'r')
#ans0 = [int(x.split(' ')[0]) for x in f.readlines()]
#f.close()

f = open('a.html', 'w')
print >>f, '<!DOCTYPE html>'
print >>f, '<html> <body>'
print >>f, '<table>'
#print >>f, '<tr>'
#print >>f, '<td align="center">Query</td>'
#print >>f, '<td align="center"></td>'
#print >>f, '<td align="center">1st Closest</td>'
#print >>f, '<td align="center">2nd Closest</td>'
#print >>f, '<td align="center">3rd Closest</td>'
#print >>f, '<td align="center">4th Closest</td>'
#print >>f, '<td align="center">5th Closest</td>'
#print >>f, '</tr>'
for i in range(min(100, len(ans))):
    std = b[i].split('_')[0]
    td = '<td align="center">'
    template = 'alt="" style="height:50px;max-width:70px" align="right"'
    print >>f, '<tr>'
    print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, b[i], template)
    print >>f, '<td width="10"></td>'
    for k in ans[i]:
        ok_icon = '<img src="ok-icon.png" alt="" style="height:15px;width:15px">' 
        flag = ok_icon if a[k].split('_')[0] == std else ''
        if k != ans[i][0]: flag = ''
        print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, a[k], template)
        print >>f, '<td>{}</td>'.format(flag)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()
