f = open('24-16-1.txt').read().split('\n')

f[-1] = f[-1]+'              '

ctr = [int(i) for i in f[0].split(',')]

cw = []

wls = (1 + len(f[2]))//4
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
#print('ls',ls)
for gs in range(100):
    for d in range(len(ctr)):
        sc = ''
        dls[d] = (dls[d] + ctr[d])%ls[d]
    #print(dls)
    scrn = ''
    scrna = ''
    for d in range(len(ctr)):
        scrn = scrn + ' ' + cw[d][dls[d]]
        scrna = scrna + cw[d][dls[d]][0] + cw[d][dls[d]][2]
    print(scrn)
    wn = calculate_points(scrna)
    trc = scrn.split()
    #if((trc[0] == trc[1]) and (trc[0] == trc[2])):
    #    cn += 1
    #    print('trio')
    #print(wn)
    cn += wn
    


