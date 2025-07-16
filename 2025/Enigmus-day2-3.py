import copy
 
f = open('day2-3.txt').read().split('\n')
 
datal = []
datar = []
datacdl = []
datacdr = []
dataid = []
 
bkl = []
bkr = []

szs = {} 

maxdepth = [0]
stb = []

def printbch(bch,dpth,strl):    
    pre = ''
    for j in range(dpth * 3):
        pre = pre + ' '
    if len(bch) > 0:
        print(pre,bch[0],bch[1])
        if dpth == strl:            
            stb.append(bch[1])
        printbch(bch[3],dpth + 1,strl)
        printbch(bch[4],dpth + 1,strl)            
        if dpth in szs:
            szs[dpth] += 1
        else: szs[dpth] = 1

def recurse(nbk,n,l,id):
    if len(nbk)==0:
        nbk.append(n)
        nbk.append(l)
        nbk.append(id)
        nbk.append([])
        nbk.append([])
    else:
        if(nbk[0] > n):
            recurse(nbk[3],n,l,id)
        else:
            recurse(nbk[4],n,l,id)

occur = [False]
maxdepth = [0]

def getbch(bch,id):
    if len(bch) > 0:    
        fd = False          
        if bch[2] == id:
            if occur[0]:
                occur[0] = False
                fd = False
            else:
                fd = True                        
            if fd:
                return copy.deepcopy(bch)                                            
        if not fd:
            rt = getbch(bch[3],id)
            if rt != None:
                return rt
            rt = getbch(bch[4],id)  
            if rt != None:
                return rt
    return None

def insertbch(bk,b,id):
    if len(bk) > 0:    
        fd = False  
        if bk[2] == id:  
            if occur[0]:
                bk[0] = b[0]
                bk[1] = b[1]
                bk[2] = b[2]
                bk[3] = b[3]
                bk[4] = b[4]                
                fd = True
                return
            else:
                occur[0] = True
        if not fd:
            insertbch(bk[3],b,id)
            insertbch(bk[4],b,id)  

for i in f:
    pts = i.split()
    if(pts[0] != 'SWAP'):
        print(pts)
        n1 = int(pts[2].split('[')[1].split(',')[0])
        n2 = int(pts[3].split('[')[1].split(',')[0])
        l1 = pts[2].split(',')[1].replace(']','')
        l2 = pts[3].split(',')[1].replace(']','')
        id = int(pts[1].split('=')[1])
        recurse(bkl,n1,l1,id)        
        recurse(bkr,n2,l2,id)
    else:
        print('pts',pts)
        sp = int(pts[1])
        print('sp',sp)
        occur[0] = False
        b1 = getbch(bkl,sp)               
        print('b1',b1)
        occur[0] = True
        b2 = getbch(bkl,sp)               
        print('b2',b2)
        occur[0] = False
        b3 = getbch(bkr,sp)
        print('b3',b3)
        occur[0] = True
        b4 = getbch(bkr,sp)
        print('b4',b4)
        print('b1',b1)
        print('b2',b2)
        if b1 == None:  # Both id's in the Right branch
            occur[0] = True
            insertbch(bkr,b4,sp)
            occur[0] = False
            insertbch(bkr,b3,sp)                    
        if b3 == None:  # Both id's in the Left branch
            occur[0] = True
            insertbch(bkl,b2,sp)
            occur[0] = False
            insertbch(bkl,b1,sp)        
        if (b1 != None) and (b3 != None):
            occur[0] = True
            insertbch(bkl,b3,sp)
            occur[0] = True
            insertbch(bkr,b1,sp)        

cd = ''
printbch(bkl,0,0)
print(szs)
mx = 0
bst = 0 
for i in range(len(szs)):
    if szs[i] > mx:
        mx = szs[i]
        bst = i
print('best',bst)
stb = []
printbch(bkl,0,bst)
print(stb)
for i in stb:
    cd = cd + i

stb = []
szs = {}

printbch(bkr,0,0)
print(szs)
mx = 0
bst = 0 
for i in range(len(szs)):
    if szs[i] > mx:
        mx = szs[i]
        bst = i
print('best',bst)
stb = []
printbch(bkr,0,bst)
print(stb)
for i in stb:
    cd = cd + i
print(cd)

