f = open('24-18-1.txt').read().split('\n')

R = len(f)
C = len(f[0])
ps = set()
w = set()
for r in range(len(f)):
    for c in range(len(f[0])):
        if f[r][c] == 'P':
            ps.add((r,c))
        if f[r][c] == '.':
            w.add((r,c))

seen = set()
Q = [((1,0),1)]
P = []
while Q:
    fl,t = Q.pop()
    for dr in [(0,1), (0,-1), (1,0), (-1,0)]:        
        rr = fl[0] + dr[0]
        cc = fl[1] + dr[1]        
        if (rr,cc) in w or (rr,cc) in ps:                     
            if (rr,cc) not in seen:                
                Q.append(((rr,cc),t+1))
                seen.add((rr,cc))
                if (rr,cc) in ps:
                    P.append(t)                                        
print('part 1',max(P))               
