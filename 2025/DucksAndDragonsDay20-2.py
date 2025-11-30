import sys
from collections import deque

f = [[x for x in i] for i in open('day20-2in.txt').read().split('\n')]

for r in range(len(f)):    
    for c in range(len(f[r])):
        if f[r][c] == 'S':
            sr = r
            sc = c
        if f[r][c] == 'E':
            er = r
            ec = c

gp = {}
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
Q = deque([])
Q.append((sr,sc,0))
SEEN = set()
while Q:
    r,c,d = Q.popleft()    
    if (r,c) == (er,ec):
        print('found',d)
        sys.exit(0)        
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    for dr,dc in DIRS:
        nr,nc = r+dr, c+dc                
        if 0 <= nr < len(f) and 0 <= nc < len(f[0]):          
          if f[nr][nc] != '.':
           if f[nr][nc] in 'TE' and f[r][c] in 'ST':                 
            if dr == 0:                
                Q.append((r+dr, c+dc, d+1))                
            if ((r+c)%2 == 0) and dr == -1:                
                Q.append((r+dr, c+dc, d+1))
            if ((1+r+c)%2 == 0) and dr == 1:                
                Q.append((r+dr, c+dc, d+1))
