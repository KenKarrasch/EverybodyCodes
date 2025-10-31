f = open('day1-3in.txt').read().split('\n\n')

pb = f[0].split('\n')
sq = f[1].split('\n')

tly = 0

bk = []

for si in range(len(sq)):
    scores = []
    for i in range((int) ((len(pb[0])+1)/2)):
        x,y, dr = i * 2, 0, 0
        while y < len(pb):        
            if sq[si][dr] == 'L':
                x -= 1
                if x < 0:
                    x += 2
            if sq[si][dr] == 'R':
                x += 1
                if x >= len(pb[0]):
                    x -= 2        
            while y < len(pb) and pb[y][x] == '.':       
                y += 1
            dr += 1
        if (((x/2) + 1) * 2) - (i + 1) > 0:                        
            scores.append((int) ((((x/2) + 1) * 2) - (i + 1)))
        else:
           scores.append(0)
    
    bk.append(scores)

cds = []

for i in bk:
    cp = i[:]
    rd = []
    for j in cp:
        if j not in rd:
            rd.append(j)
    rd.sort()
    sx = 0
    nc = []
    for tk in range(len(cp)):
        if cp[tk] >= sx:
            nc.append(tk)
    cds.append(nc)

def dup(ns):
    return len(ns) != len(set(ns))
    
hg = 0
lw = 10000000

for i in range(len(cds[0])):
  print('scanned', i, 'of',len(cds[0]) )
  for j in range(len(cds[1])):
    for k in range(len(cds[2])):
      for l in range(len(cds[3])):
        for m in range(len(cds[4])):
          for n in range(len(cds[5])):
            if not dup([i,j,k,l,m,n]):
              am = bk[0][i] + bk[1][j] + bk[2][k] + bk[3][l] + bk[4][m] + bk[5][n]
              if am > hg:
                  print('new high',i,j,k,l,m,n,'sum',sum([i,j,k,l,m,n]))
                  hg = am
              if am < lw:
                  print('new low',i,j,k,l,m,n,'sum',sum([i,j,k,l,m,n]))
                  lw = am
print(lw,hg)
