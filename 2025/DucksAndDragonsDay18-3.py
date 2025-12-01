import sys
from collections import deque

f = open('day18-3in.txt').read().split('\n\n')
trk = [0]*(len(f)-1)
sm = 0
sz = len(f[-1].split('\n')[1:])
bts = [0]*sz
mx = []
def d2b(n):
    bits = []
    if n == 0:
        return [0]
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    return bits[::-1]  
sq = [0]*sz
pfm = []
for nm in range(sz):    
    plts = [0]*(len(f)-1)
    sqn = d2b(nm)    
    for i in range(len(sq)):
        if i < len(sqn):
            sq[i] = sqn[i]    
    sq = [0]*sz
    sq[nm] = 1
    for i in f[:-1]:
        p = i.split('\n')
        pn = int(p[0].split()[1])-1 
        trk[pn] = int(p[0].split()[4][:-1])
        br = 0           
        for pt in p[1:]:        
            if pt.split()[1] != 'free':        
                br += plts[int(pt.split()[4])-1] * int(pt.split()[7])
            else:
                if sq[pn] == 1:
                    br = 1 
                else:
                    br = 0
        plts[pn] = br
    mx.append(plts[-1])
    pfm.append((plts[-1],nm))
pfm.sort(reverse=True)
unm = 0
for i in pfm:
    if i[0] >= 0:
        unm += 2**i[1]
pfm = []
for nm in [unm]:    
    plts = [0]*(len(f)-1)
    sqn = d2b(nm)    
    for i in range(len(sq)):
        if i < len(sqn):
            sq[i] = sqn[i]    
    sq = sq[::-1]
    for i in f[:-1]:
        p = i.split('\n')
        pn = int(p[0].split()[1])-1 
        trk[pn] = int(p[0].split()[4][:-1])
        br = 0           
        for pt in p[1:]:        
            if pt.split()[1] != 'free':
                br += plts[int(pt.split()[4])-1] * int(pt.split()[7])
            else:
                if sq[pn] == 1:
                    br = 1 
                else:
                    br = 0
        if br < trk[pn]:
            br = 0
        plts[pn] = br
    mx.append(plts[-1])    
best = plts[-1]
tly = 0
for i in f[-1].split('\n')[1:]:
    plts = [0]*(len(f)-1)
    sq = [int(x) for x in i.split()]
    for i in f[:-1]:
        p = i.split('\n')
        pn = int(p[0].split()[1])-1 
        trk[pn] = int(p[0].split()[4][:-1])
        br = 0           
        for pt in p[1:]:        
            if pt.split()[1] != 'free':                
                br += plts[int(pt.split()[4])-1] * int(pt.split()[7])
            else:
                if sq[pn] == 1:
                    br = 1 
                else:
                    br = 0
        if br < trk[pn]:
            br = 0
        plts[pn] = br
    mx.append(plts[-1])
    if plts[-1] > 0:
        tly += best - plts[-1]
print(tly)
