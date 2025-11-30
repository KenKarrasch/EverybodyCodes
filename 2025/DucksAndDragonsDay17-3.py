from collections import deque

import heapq
#from math import inf

f = open('day17-3in2.txt').read().split('\n')

rc = (int) (len(f[0])/2)
cc = (int) (len(f)/2)

for r in range(len(f)):
  for c in range(len(f[r])):
    if '@' in f[r][c]:      
      mr = r
      mc = c

lv = 10
num = '0123456789'
st = []
ed = []

dn = False
for rd in range(1,mr):  
 if not dn:
  lv = rd  
  lna = {}
  for r in range(len(f)):
   ln = ''   
   for c in range(len(f[r])):
     if f[r][c] == 'S':
        st = (r,c,0)
        ed = (r,c,4)
     dr = r-rc
     dc = c-cc
     if (dr*dr) + (dc*dc) <= lv*lv:             
       ln = ln + ' '          
     else:
       ln = ln + f[r][c]   
       if r == mr:
         if c < mc:
            lna[(r,c,1)] = int(f[r][c])   
         else:
            lna[(r,c,3)] = int(f[r][c])                  
       else:
        if r < mr:
          if f[r][c] in num:
            lna[(r,c,0)] = int(f[r][c])
            lna[(r,c,4)] = int(f[r][c])
          else:
            lna[(r,c,0)] = 0
            lna[(r,c,4)] = 0          
        if r > mr:
          lna[(r,c,2)] = int(f[r][c])          
  if True:

    sx, sy, sz = st[0],st[1],st[2]
    gx, gy, gz = ed[0],ed[1],ed[2]

    dist = {}
    for i in lna:
       dist[(i[0],i[1],i[2])] = 999999999
    
    dist[(st[0],st[1],st[2])] = 0

    pq = [(dist[(st[0],st[1],st[2])], (sx, sy, sz) )]  # (time, x, y)

    # 4-directional moves
    #directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    directions = [(-1,0,0),(0,1,0),(1,0,0),(0,-1,0),
        (-1,0,1),(0,1,1),(1,0,1),(0,-1,1),
        (-1,0,-1),(0,1,-1),(1,0,-1),(0,-1,-1)]

    while pq:
        #print(len(pq))        
        cur_time, xyz = heapq.heappop(pq)
        #print 'popped',cur_time, xyz
        x, y, z = xyz[0], xyz[1], xyz[2]
        # Early exit if we reached the goal
        if (x, y, z) == (gx, gy, gz):
            print('found',cur_time,rd+1)
            if cur_time < (rd+1)*30:
             print('made it',cur_time,rd+1,(rd+1)*30)
             print cur_time*rd
             dn = True
            break

        # Skip if we already found a better path
        if cur_time > dist[(x,y,z)]:
            #print('better',dist[(x,y,z)])
            continue

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            #print 'checking',nx, ny, nz,dx, dy, dz
            if (nx,ny,nz) in lna:
              new_time = cur_time + lna[(nx,ny,nz)]
              if new_time < dist[(nx,ny,nz)]:
                  dist[(nx,ny,nz)] = new_time
                  #print('adding', (new_time, (nx, ny, nz)))
                  heapq.heappush(pq, (new_time, (nx, ny, nz)))
