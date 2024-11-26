f = open('24-16-3.txt').read().split('\n')

# Takes a few minutes on the phone python app.
# Started 13 hrs late but still managed to get 82 on the global leaderboard

ltrs = len(f[2])
for i in range(2,len(f)):
    if(len(f[i]) < ltrs):
        for gz in range(ltrs):
            f[i] = f[i] + ' '

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
            #print(cw)

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

def pull_llever_plus(dls):
    for d in range(len(ctr)):        
        dls[d] = (dls[d] + 1)%ls[d]    
    return dls

def pull_llever_minus(dls):    
    for d in range(len(ctr)):            
        dls[d] = (ls[d]+dls[d] - 1)%ls[d]        
    return dls

def pull_rlever(dls):
    for d in range(len(ctr)):
        dls[d] = (dls[d] + ctr[d])%ls[d]    
    return(dls)
    #trc = scrn.split()
    #if((trc[0] == trc[1]) and (trc[0] == trc[2])):
    #    cn += 1
    #    print('trio')
    #print(wn)
def showscrn(dls):
    scrn = ''
    scrna = ''    
    for d in range(len(ctr)):    
        scrn = scrn + ' ' + cw[d][dls[d]]
        scrna = scrna + cw[d][dls[d]][0] + cw[d][dls[d]][2]
    print(scrn)    
    wn = calculate_points(scrna)
    return wn

def calccoin(dls):
    scrn = ''
    scrna = ''    
    for d in range(len(ctr)):    
        scrn = scrn + ' ' + cw[d][dls[d]]
        scrna = scrna + cw[d][dls[d]][0] + cw[d][dls[d]][2]
    #print(scrn)    
    wn = calculate_points(scrna)
    return wn


DB = [(dls,0,0)]
mx = 0
mn = 100000000000000000000000000000000

DP = {}


while len(DB) > 0:
    dls, cn, pls = DB.pop()
    skip = False
    #print(len(DB))
    if((dls[0],dls[1],dls[2],pls) in DP.keys()):
        if(DP[(dls[0],dls[1],dls[2],pls)] >= cn):
            #print('skip')
            skip = True
        else:
            DP[(dls[0],dls[1],dls[2],pls)] = cn            
    else:        
        DP[(dls[0],dls[1],dls[2],pls)] = cn

    if not skip:
        if(pls == 256):
            print(mx)
            mx = max(mx,cn)
            #mn = min(mn,cn)
        else:
            sdls = dls[:]


            dls = sdls[:]
            #Option 2
            dls = pull_llever_plus(dls)
            dls = pull_rlever(dls)        
            nwn = calccoin(dls)    
            DB.append((dls[:],cn+nwn,pls+1))


            dls = sdls[:]
            #Option 3
            dls = pull_llever_minus(dls)
            dls = pull_rlever(dls)        
            nwn = calccoin(dls)
            DB.append((dls[:],cn+nwn,pls+1))

            dls = sdls[:]
            #Option 1    
            dls = pull_rlever(dls)    
            nwn = calccoin(dls)
            DB.append((dls[:],cn+nwn,pls+1))

#564


DP = {}

DB = [(dls,0,0)]

while len(DB) > 0:
    dls, cn, pls = DB.pop()
    skip = False
    #print(len(DB))
    if((dls[0],dls[1],dls[2],pls) in DP.keys()):
        if(DP[(dls[0],dls[1],dls[2],pls)] <= cn):
            #print('skip')
            skip = True
        else:
            DP[(dls[0],dls[1],dls[2],pls)] = cn            
    else:        
        DP[(dls[0],dls[1],dls[2],pls)] = cn

    if not skip:
        if(pls == 256):
            print(mn)
            #mx = max(mx,cn)
            mn = min(mn,cn)
        else:
            sdls = dls[:]

            dls = sdls[:]
            #Option 3
            dls = pull_llever_minus(dls)
            dls = pull_rlever(dls)        
            nwn = calccoin(dls)
            DB.append((dls[:],cn+nwn,pls+1))


            dls = sdls[:]
            #Option 2
            dls = pull_llever_plus(dls)
            dls = pull_rlever(dls)        
            nwn = calccoin(dls)    
            DB.append((dls[:],cn+nwn,pls+1))


            dls = sdls[:]
            #Option 1    
            dls = pull_rlever(dls)    
            nwn = calccoin(dls)
            DB.append((dls[:],cn+nwn,pls+1))


print(mx, mn)
