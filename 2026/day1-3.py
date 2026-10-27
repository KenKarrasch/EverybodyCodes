import math
f = [int(x) for x in open('day1-3.txt').read().split(',')]

bk = []
dn = False
for ti in range(1,max(f)):
    if not dn:
        i = 1 + ti * 2
        if (i*i) - 1 > f[-1] + 10000:
            dn = True
        bk.append((i*i) -1) 
tly = 0
for i in f: 
    pb = 0   
    dn = False
    for b in bk:
        if not dn:
            if i <= b:                    
                np = b - i 
                dn = True            
    tly += np
print('tly',tly)
