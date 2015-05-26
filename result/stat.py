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
lines = f.readlines()
ans = [x.split(' ')[1::2] for x in lines]
ans = [[int(i) for i in x] for x in ans]
access_nums = [int(x.split(' ')[0]) for x in lines]
f.close()
assert(len(ans) == len(b))

print 'tree:'
print '  #queries:', len(access_nums)
print '  #access:', sum(access_nums) / float(len(access_nums))

cnt = 0
cnt2 = 0
for i in range(len(ans)):
    x = b[i].split('_')[0]
    y = a[ans[i][0]].split('_')[0]
    if x == y:
        cnt += 1
    for k in ans[i]:
        y = a[k].split('_')[0]
        if x == y:
            cnt2 += 1
            break

print 'result:'
print '  #queries:', len(ans)
print '  #correct_first:', cnt, '  <- if found closest is correct'
print '  #correct_total:', cnt2, '  <- if found top-K closest is correct'
