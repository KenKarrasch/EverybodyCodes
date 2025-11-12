f = open('day7-3in.txt').read().split('\n\n')

nms = f[0].split(',')
rls = [y.split(' > ') for y in f[1].split('\n')]

cds = []
for i in rls:
    for cd in i[0]:
        cds.append(cd)
    for cd in i[1].split(','):
        if cd not in cds:
            cds.append(cd)

cdsd = {}
for i in rls:
    cdsd[i[0]] = i[1].split(',')

cmbo = {}

def getcombo(lt,dpth,tlt):
    if dpth == 0:
        return 1
    if (lt,dpth) in cmbo:
        return cmbo[(lt,dpth)]    
    cb = 0
    if lt in cdsd: 
        for nc in cdsd[lt]:  
            cb += getcombo(nc,dpth-1,tlt + nc)    
    return cb

for d in range(12):
    for l in cds:        
        cmbo[(l,d)] = getcombo(l,d,l)

def pok(l1,l2):    
    for i in rls:
        if l1 == i[0] and l2 in i[1]:
            return True
    return False
            
def gs(s):    
    for l in range(len(s)-1):
        if not pok(s[l],s[l+1]):
            return False
    return True

nnms = []
tly = 0
nms.sort()

for i in nms:
    ok = True
    for j in nms:
        if i != j:
            if j in i:
                ok = False
    if ok:
        nnms.append(i)

for i in nnms:
    if gs(i):
        for lt in range(7,12):
            tly += cmbo[(i[-1], lt-len(i))]
print(tly)
