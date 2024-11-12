f = open('24-2-1.txt').read().split('\n')
t = []
bst = []
bstd = []

for i in range(len(f)):    
    br = f[i].split(':')
    l = br[1].split(',')
    brs = []
    brs.append(br[0])
    lks = []
    for ls in l:
        lks.append(ls)
    brs.append(lks)    
    t.append(brs)


def sch(lf,dpth,pth):
    if(lf == '@'): 
        bst.append(dpth)
        bstd.append(pth)        
    for i in range(len(t)):  
        if t[i][0] == lf:
            for sc in t[i][1]:
                npth = pth[:]
                npth.append(sc)                
                sch(sc, dpth + 1,npth)

lvs = []  
for i in range(len(t)):      
    for sc in t[i][1]:
        if (sc not in lvs):
            lvs.append(sc)

sch('RR',0,['RR'])
best = -1
for i in range(len(bst)):    
    ct = 0
    for j in range(len(bst)):
        if(i != j):
            if(bst[i] == bst[j]):
                ct += 1
    if (ct == 0):        
        best = i
bststr = ''
for i in bstd[best]:
    bststr = bststr + i[1]
print('part 2 -', bststr)
