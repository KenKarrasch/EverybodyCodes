f = open('24-3-3.txt').read().split('\n')
# Yay! for part 3 my time managed to clock in at rank no 4 on the global leaderboard! 
# (of course the time was done post event, there is probably heaps 
# of others who did it just as fast, may as well enjoy the glory, even if it is illusory)

grd = [[0 for i in range(len(f[0])+2)]]
dn = False

for i in f:
    ln = [0]
    for h in i:
        if h == '#':
            ln.append(1)
        else:
            ln.append(0)
    ln.append(0)
    grd.append(ln)

grd.append([0 for i in range(len(f[0])+2)])

dr = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]

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
                if(grd[i][j] == ht):
                    grd[i][j] += 1
    return done

ht = 0
dn = False
while not dn:
    ht += 1
    dn = dogrid(ht)
    for i in grd[0:30]:
        ln  = ''
        for j in i:
            ln = ln + str(j)
        print(ln) 
    print()


ty = 0
for i in range(len(grd)):    
    for j in range(len(grd[0])):            
            ty += grd[i][j]

print('part 3 -',ty)
