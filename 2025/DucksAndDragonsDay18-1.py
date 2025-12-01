from collections import deque

f = open('day18-1in.txt').read().split('\n\n')

trk = [0]*len(f)
plts = [0]*len(f)

for i in f:
    p = i.split('\n')
    pn = int(p[0].split()[1])-1 
    trk[pn] = int(p[0].split()[4][:-1])
    br = 0   
    for pt in p[1:]:        
        if pt.split()[1] != 'free':
           br += plts[int(pt.split()[4])-1] * int(pt.split()[7])
        else:
            br = 1 
    if br < trk[pn]:
        br = 0
    plts[pn] = br
print(max(plts))
