from collections import deque

f = open('24-18-3.txt').read().split('\n')

R = len(f)
C = len(f[0])

ps = set()
w = set()
W = {}
sts = []
for r in range(len(f)):
    for c in range(len(f[0])):
        if f[r][c] == 'P':
            ps.add((r,c))            
        if f[r][c] == '.':
            w.add((r,c))
            W[(r,c)] = 0
            if c == 0 or c == C-1:
                sts.append((r,c))

ct = 0
for pes in ps:
    ct += 1
    seen = set()
    print(ct,'of',len(ps))
    Q = deque([((pes),1)])
    p = 0
    P = []       
    while Q:
        fl,t = Q.popleft()        
        for dr in [(0,1), (0,-1), (1,0), (-1,0)]:        
            rr = fl[0] + dr[0]
            cc = fl[1] + dr[1]            
            if (rr,cc) in w or (rr,cc) in ps:                     
                if (rr,cc) not in seen:                    
                    Q.append(((rr,cc),t+1))
                    seen.add((rr,cc))
                    if (rr,cc) in W.keys():                        
                            W[(rr,cc)] += t
                    if (rr,cc) in ps:
                        P.append(t)           

bst = []
for k,v in W.items():
    bst.append((v,k))
bst.sort()
print('best',bst[0])

seen = set()
Q = deque([(bst[0][1],1)])
P = []

while Q:
    fl,t = Q.popleft()
    print(fl,t)        
    for dr in [(0,1), (0,-1), (1,0), (-1,0)]:        
        rr = fl[0] + dr[0]
        cc = fl[1] + dr[1]        
        if (rr,cc) in w or (rr,cc) in ps:                     
            if (rr,cc) not in seen:                
                Q.append(((rr,cc),t+1))
                seen.add((rr,cc))
                if (rr,cc) in ps:
                    P.append(t)                                        
print('part 3',sum(P))
