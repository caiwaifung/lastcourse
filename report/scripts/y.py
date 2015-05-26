import matplotlib.pylab as plt
import numpy as np
import sys

f = open('a.txt', 'r')
a = f.readlines()
f.close()

xs = [c[:-2] for c in a[::2]]
ys = [c.strip().split(' ')[-1] for c in a[1::2]]
assert(len(xs) == len(ys))
xs = zip(xs, ys)
xs = [(x.split('-')[1], y) for (x, y) in xs if x.split('-')[0]=='5']

def sp(x):
    y = ''
    while len(x) > 0 and x[-1].isdigit():
        y = x[-1] + y
        x = x[:-1]
    return (x, int(y))

xs = [(sp(x)[1], sp(x)[0], y) for (x, y) in xs]
xs = sorted(xs)


plt.figure(1, figsize=(9, 5))
fs = np.unique(sorted([x[1] for x in xs]))
for f in fs:
    cx = []
    cy = []
    for x in xs:
        if x[1] == f:
            cx.append(float(x[0]))
            cy.append(float(x[2]))
    plt.plot(cx, cy, 'o-', label=f)
plt.xlabel('Feature Number')
plt.ylabel('Node Access Number')
plt.grid()
plt.legend(loc='upper left')
plt.savefig('../data/accessnum.pdf')

