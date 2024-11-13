f1 = open('24-3-1.txt').read().split('\n')
f2 = open('24-3-2.txt').read().split('\n')
# Based on my times I managed to get global leaderboard
# Rank 20 for part 1
# Rank 5 for part 2
# Rank 4 for part 3

dr = [[0,1],[0,-1],[1,0],[-1,0]]

def checkones(x,y,ht):
    gd = True
    for d in dr:
        if grd[x+d[0]][y+d[1]] < ht:
            gd = False
    return gd

def dogrid(ht):
    done = True
    for i in range(1,len(grd)-1):
        for j in range(1,len(grd[0])-1):
            if(checkones(i,j,ht)):
                done = False
                grd[i][j] += 1
    return done

grd = []
for i in f1:
    ln = []
    for h in i:
        if h == '#':
            ln.append(1)
        else:
            ln.append(0)
    grd.append(ln)

ht = 0
dn = False
while not dn:
    ht += 1
    dn = dogrid(ht)

ty = 0
for i in range(len(grd)):
    for j in range(len(grd[0])):
            ty += grd[i][j]

print('part 1 -',ty)

grd = []
for i in f2:
    ln = []
    for h in i:
        if h == '#':
            ln.append(1)
        else:
            ln.append(0)
    grd.append(ln)

ht = 0
dn = False
while not dn:
    ht += 1
    dn = dogrid(ht)

ty = 0
for i in range(len(grd)):
    for j in range(len(grd[0])):
            ty += grd[i][j]

print('part 2 -',ty)
