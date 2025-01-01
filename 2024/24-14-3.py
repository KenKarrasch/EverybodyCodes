r,c = 0,0from collections import defaultdict, deque

fn = open('24-14-3.txt').read().split('\n')

dr = {'U': (1,0,0), 'D': (-1,0,0), 'L': (0,-1,0), 'R': (0,1,0),'F': (0,0,1), 'B': (0,0,-1)}

ht = []

sgs = set()
lf = set()
last = 'U'
for b in fn:
    f = b.split(',')
    r,c,z = 0,0,0
    for i in f:  
        d = i[0]        
        for s in range(int(''.join(i[1:]))):
            r += dr[d][0]            
            if (r,c,z) not in sgs:
                sgs.add((r,c,z))
        for s in range(int(''.join(i[1:]))):
            c += dr[d][1]            
            if (r,c,z) not in sgs:
                sgs.add((r,c,z))        
        for s in range(int(''.join(i[1:]))):
            z += dr[d][2]            
            if (r,c,z) not in sgs:
                sgs.add((r,c,z))   
        ht.append(r)        
    lf.add((r,c,z))
print(lf)
print(max(ht))
fd = []
mds = []
for hgt in range(1,max(ht)):    
    if (hgt,0,0) in sgs:        
        seen = set()
        lc = 0
        mk = 0
        Q = deque([(0,hgt,0,0)])         
        while Q or lc < len(lf):            
            d,r,c,z = Q.popleft()
            if (r,c,z) in seen:
                continue
            seen.add((r,c,z))   
            if (r,c,z) in lf:
                lc += 1                
                mk += d                                
            for drt in dr.keys():     
                if (r+dr[drt][0],c+dr[drt][1],z+dr[drt][2]) in sgs:                      
                    Q.append((d+1,r+dr[drt][0],c+dr[drt][1],z+dr[drt][2]))
        mds.append(mk)

print(min(mds))

