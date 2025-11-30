import sys
from collections import deque
import math

# Took a while to realise the end point is not the centroid.

f = [[x for x in i] for i in open('day20-3in.txt').read().split('\n')]

for r in range(len(f)):    
    for c in range(len(f[r])):
        if f[r][c] == 'S':
            sr,sc = r,c            
        if f[r][c] == 'E':
            er,ec = r,c            

sz = len(f[0])
gp = {}

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

discnums = []

def rotate(x, y, angle):
    theta = math.radians(angle)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x_new = x * cos_t - y * sin_t
    y_new = x * sin_t + y * cos_t
    return x_new, y_new

def sdiscnum(cn):
    if cn not in discnums:
        discnums.append(cn)   

for r in range(len(f)):    
    for c in range(len(f[r])):     
     if f[r][c] != '.':
      pl = []            
      for dr,dc in DIRS:        
        nr,nc = r+dr, c+dc    
        if 0 <= nr < len(f) and 0 <= nc < len(f[0]):                    
          if f[nr][nc] != '.':    
            if dr == 0:         
              if dc == 1:                
                if (r+c)%2 == 0:                   
                   pl.append((nr,nc,120))
                else:
                   pl.append((nr,nc,60))
              if dc == -1:                
                if (r+c)%2 == 0:                   
                   pl.append((nr,nc,240))
                else:
                   pl.append((nr,nc,300))
            if ((r+c)%2 == 0) and dr == -1:                             
                pl.append((nr,nc,0))
            if ((1+r+c)%2 == 0) and dr == 1:                                         
                pl.append((nr,nc,180))
      gp[(r,c)] = pl

cd = {}
cdi = {}

Q = deque([])
cr = len(f)//3
cc = len(f[0])//2
Q.append((cr,cc,0,0,True))
SEEN = set()
while Q:
    r,c,rr,rc,d = Q.popleft()    
    rdrr = round(rr,8)
    rdrc = round(rc,8)
    sdiscnum(rdrr)
    sdiscnum(rdrc)
    cd[(r,c)] = (rdrr,rdrc)

    cdi[(rdrr,rdrc)] = (r,c)
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))    
    for nr,nc,ang in gp[(r,c)]:            
        if f[nr][nc] in '#TES':     
            nrc, nrr = rotate(1, 0, ang)
            Q.append((nr, nc, nrr+rr, nrc+rc,not d))     


def discise(rtr,ctr):
   rtrr, ctrr = 0 , 0 
   for i in discnums:
      if i - 0.000001 < rtr < i + 0.000001:
         rtrr = i
      if i - 0.000001 < ctr < i + 0.000001:
         ctrr = i
   return rtrr,ctrr

Q = deque([])
Q.append((sr,sc,0,0))
SEEN = set()
while Q:
    r,c,d,rot = Q.popleft()     
    if (r,c) == (er,ec):
        print('found',d)
        sys.exit(0)        
    if (r,c,rot%3) in SEEN:
        continue
    SEEN.add((r,c,rot%3))
    dsts = gp[(r,c)][:]
    dsts.append((r,c,0))
    for nr,nc,ang in dsts:                    
        rr,rc = cd[(nr,nc)]
        nrr,nrc = rotate(rr,rc,120)
        nr,nc = cdi[discise(nrr,nrc)]
        if f[nr][nc] in 'TE' and f[r][c] in 'ST':     
            Q.append((nr, nc, d+1,rot+1))               
