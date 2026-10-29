import math

f = open('in1.txt').read().split('\n')

tly = 0
for i in f:
    print(i)
    n = 0
    p,nm = i.split('-')[1].split()
    for i in range(4):
        print(int(nm[i]))
        print(int(p[i]))
        bt = int(nm[i])*math.pow(int(p[i]),3-i)
        n += bt
        print('bt',bt)
    print('n',n)
    tly += n
print('tly',tly)
