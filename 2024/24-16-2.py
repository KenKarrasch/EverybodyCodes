f = open('24-16-2.txt').read().split('\n')


ltrs = len(f[2])
for i in range(2,len(f)):
    if(len(f[i]) < ltrs):
        for gz in range(ltrs):
            f[i] = f[i] + ' '

ctr = [int(i) for i in f[0].split(',')]

cw = []

wls = (1 + len(f[2]))//4
print(wls)
for i in range(wls):
    cw.append([])

for i in range(2,len(f)):    
    cts = f[i]
    for j in range(wls):        
        if(cts[4*j] != ' '):
            cw[j].append(cts[4*j:4*j + 3])

print(cw)

ls = []
for i in cw:
     ls.append(len(i))

def calculate_points(s):
    cl = {}
    for i in s:
        if(i in cl.keys()):
            cl[i] = cl[i] + 1
        else:
            cl[i] = 1
    vs = cl.values()
    cns = 0
    for i in vs:
        if i > 2:
            cns += i-2
    return cns

dls = []
for i in range(wls):
    dls.append(0)
cn = 0
fcn = 0
#print('ls',ls)
ptn = {}
lstc = 0
dn = False
gs = 0
fgs = 0
mem = []
rm = False
rsgn = ''
foundfirst = False
while not dn:    
#for gs in range(1000000):
    gs += 1
    for d in range(len(ctr)):
        sc = ''
        dls[d] = (dls[d] + ctr[d])%ls[d]
    #print(dls)
    scrn = ''
    scrna = ''
    sgn = ''
    for d in range(len(ctr)):
        scrn = scrn + ' ' + cw[d][dls[d]]
        scrna = scrna + cw[d][dls[d]][0] + cw[d][dls[d]][2]
        sgn = sgn + ',' + str(dls[d])
    
    wn = calculate_points(scrna)
    trc = scrn.split()
    
    #if((trc[0] == trc[1]) and (trc[0] == trc[2])):        
        #wn += 1
        #print('trio')
    #print(wn)
    cn += wn

    if rm:
        mem.append(cn-fcn)

    if(sgn == rsgn):
        print(gs)
        cyclelength = gs-fgs
        print('fcn',fcn,'cn',cn)
        print('cyclelength',cyclelength)
        gl = 202420242024 - gs
        leaps = gl//cyclelength
        print('leaps',leaps)
        leftover = gl%cyclelength
        print('leftover',leftover)
        print(len(mem))
        print('mem[leftover]',mem[leftover])
        changecn = cn-fcn
        tot = cn + leaps*changecn + mem[leftover]
        print(tot-1)
        dn = True
    #print(sgn,rsgn)
    if(sgn in ptn.keys()):
        if not foundfirst:
            print('cycle',sgn)  
            print(scrna,gs,cn,ptn[sgn])    
            foundfirst = True
            rsgn = sgn
            fgs = gs
            fcn = cn
            rm = True
        
    else:
        ptn[sgn] = cn

