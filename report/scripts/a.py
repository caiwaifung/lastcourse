import sys

f = open('b.txt', 'r')
a = f.readlines()
f.close()

xs = [c[:-2] for c in a[::2]]
ys = [c.strip().split(' ')[-1] for c in a[1::2]]
for x in xs:
    i = int(x.split('-')[0])
    cur = x.split('-')[1]
    if i != 1:
        continue
    print cur, 
    for z in [1,2,3,4,5]:
        flag = False
        for k in range(len(xs)):
            x2 = xs[k]
            if int(x2.split('-')[0]) == z and x2.split('-')[1] == cur:
                print '&', ys[k],
                flag = True
                break
        if not flag:
            print 'ERROR'
            sys.exit(1)
    print '\\\\ \\hline'
