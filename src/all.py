import os

a = []
a.append(('ColorMomentHSV9', 9))
for k in [4, 8, 12, 16, 20, 24, 30]:
    a.append(('PCA{}'.format(k), k))
for k in [4, 8, 12, 16, 20, 24]:
    a.append(('KMeans{}'.format(k), k))
for k in [25]:
    a.append(('Composite{}'.format(k), k))

for d in [1, 2, 3, 4, 5]:
    for x in a:
        print '{}-{}:'.format(d,x[0])
        cmd_r = 'python run.py a {} data{}k {}'.format(x[0], d,x[1])
        #cmd_g = 'grep "#cor\|#access\|#split"'
        cmd_g = 'grep "#correct_first"'
        os.system('{} | {}'.format(cmd_r, cmd_g))

