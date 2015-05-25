import os

p = dict()


f = open('./color_feature.txt', 'r')
g = open('./imagelist.txt', 'r')
f.readline()
f.readline()

for s in g.readlines():
        p[s.strip()] = f.readline()[5:]
f.close()
g.close()

def gen_trans(ss):
        f = open('../' + ss + '.txt', 'r')
        g = open('./' + ss + '.feature', 'w')
        lines = f.readlines()
        g.write(str(len(lines)) + ' 9\n')
        for s in lines:
                s = s.strip()
                g.write(p[s])
        g.close()
        f.close()

gen_trans('data1k')
gen_trans('data2k')
gen_trans('data3k')
gen_trans('data4k')
gen_trans('data5k')
gen_trans('query')
