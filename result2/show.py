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

#labels = ['',
#    'n01613177', 'n01923025', 'n02278980', 'n03767203', 'n03877845',
#    'n04515003', 'n04583620', 'n07897438', 'n10247358', 'n11669921']
#
#f = open('../result/res.txt', 'r')
#lines = f.readlines()
#f.close()
#res = [int(line.split(',')[0]) for line in lines]
#res = [labels[i] for i in res]
#ans = []
#for label in res:
#    cur = []
#    for i in range(len(a)):
#        if a[i].split('_')[0] == label:
#            cur.append(i)
#            if len(cur) >= 3:
#                break
#    ans.append(cur)
f = open('../result2/final.txt', 'r')
ans = [line.strip() for line in f.readlines()]
def func(x):
    r = x[0:3]
    rs = set(r)
    for i in x[10:13]:
        if not i in rs:
            r.append(i)
            rs.add(i)
            if len(r) >= 5:
                break
    return r
ans = [func([int(x) - 1 for x in line.split(',')]) for line in ans]
#ans = [[int(line.strip().split(',')[0]) - 1] for line in ans]
f.close()


#f = open('ans0.txt', 'r')
#ans0 = [int(x.split(' ')[0]) for x in f.readlines()]
#f.close()
cnt = 0
cnt2 = 0
for i in range(len(ans)):
    k = ans[i][0]
    cur = a[k].split('_')[0]
    std = b[i].split('_')[0]
    if cur == std:
        cnt += 1
    for k in ans[i]:
        cur = a[k].split('_')[0]
        if cur == std:
            cnt2 += 1
            break

print 'correct: ', cnt
print 'accuracy:', int(float(cnt) / float(len(ans)) * 10000) / 100., '%'
print 'correct2: ', cnt2
print 'accuracy2:', int(float(cnt2) / float(len(ans)) * 10000) / 100., '%'


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
for i in range(min(300, len(ans))):
    std = b[i].split('_')[0]
    td = '<td align="center">'
    template = 'alt="" style="height:150px;max-width:200px" align="right"'
    print >>f, '<tr>'
    print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, b[i], template)
    print >>f, '<td width="10"></td>'
    for k in ans[i]:
        ok_icon = '<img src="ok-icon.png" alt="" style="height:15px;width:15px">' 
        flag = ok_icon if a[k].split('_')[0] == std else ''
        print >>f, '{}<img src="../data/image/{}" {}></td>'.format(td, a[k], template)
        print >>f, '<td>{}</td>'.format(flag)
    print >>f, '</tr>'
print >>f, '</table>'
print >>f, '</body> </html>'
f.close()

