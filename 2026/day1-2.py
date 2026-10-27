import math
f = [int(x) for x in open('day1-2.txt').read().split(',')]
bk = []
for i in range(3,max(f)):
    bk.append(i*2 + (i-2)*2) 
tly = 0
for i in f: 
    dn = False
    for b in bk:
        if not dn:
            if i <= b:                    
                np = b - i 
                dn = True            
    tly += np
print('tly',tly)
