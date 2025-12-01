import sys
from collections import deque

f = open('day18-2in.txt').read().split('\n\n')

trk = [0]*(len(f)-1)
sm = 0

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
    sm += plts[-1]
print(sm)

