f = open('day2-2.txt').read().split('\n')

lt = []
nt = []
mdpth = []
idsl = {}
idsr = {}
nums = []
flips = []

def addtotree(ltb,id,num,ltr):
    if len(ltb) == 0:        
        ltb.append([(id,num,ltr),[],[]])     
        flips.append(False)   
    else:
        if num > ltb[0][0][1]:
            addtotree(ltb[0][2],id,num,ltr)
        else:
            addtotree(ltb[0][1],id,num,ltr)

def addnode(id,n,side):
    pts = n.split(',')
    num = int(pts[0].replace('[',''))   
    if num in nums:
        nums.append(-1)
    else:
        nums.append(num)
    ltr = pts[1].replace(']','')
    if side == 'left':        
        addtotree(lt,id,num,ltr)
        idsl[id] = (num,ltr)
    else:
        addtotree(nt,id,num,ltr)
        idsr[id] = (num,ltr)

def printbch(bch,dpth):
    pre = ''
    for j in range(dpth * 3):
        pre = pre + ' '
    if(len(bch) > 0):
        print(pre,bch[0][0])
        printbch(bch[0][1],dpth + 1)
        printbch(bch[0][2],dpth + 1)
    mdpth.append(dpth)

def replaceid(bch,id,num,ltr):
    if(len(bch) > 0):        
        if id == bch[0][0][0]:
            bch[0][0] = (id,num,ltr)
        else:
            replaceid(bch[0][1],id,num,ltr)
            replaceid(bch[0][2],id,num,ltr)

        

for i in f:
    if len(i.split()) > 2:
        bts = i.split()[2:4]            
        id = int(i.split()[1].split('=')[1])        
        #print('id',id)
        addnode(id,bts[0].split('=')[1],'left')    
        addnode(id,bts[1].split('=')[1],'right')    
    else:        
        id = int(i.split()[1])
        if not flips[id]:        
            num,ltr = idsr[id]
            #print('replacing',id,num,ltr)
            replaceid(lt,id,num,ltr)        
            #printbch(lt,0)   
            num,ltr = idsl[id]
            #print(num,ltr)
            #print('replacing',num,ltr)
            replaceid(nt,id,num,ltr)        
            #printbch(lt,0)   
        else:
            num,ltr = idsl[id]            
            replaceid(lt,id,num,ltr)                    
            num,ltr = idsr[id]            
            replaceid(nt,id,num,ltr)        
        if flips[id]: flips[id] = False
        else: flips[id] = True
        

#print(idsl.values())
printbch(lt,0)
#print(max(mdpth))
#mdpth = []
printbch(nt,0)

ltrs = []
for i in range(max(mdpth)):
    ltrs.append([])

def getltrs(bch,dpth):    
    if(len(bch) > 0):     
        #print('----')
        #print(dpth)
        #print(len(ltrs))
        #print(bch)
        ltrs[dpth].append(bch[0][0][2])
        getltrs(bch[0][1],dpth + 1)
        getltrs(bch[0][2],dpth + 1)
    

getltrs(lt,0)
#print(ltrs)
for i in ltrs:
    print(len(i),i)


def getbst(ltrs):
    bst = []
    for i in ltrs:
        if len(bst) < len(i):
            bst = i[:]
    print(bst)
    return bst


getbst(ltrs)

ans = ''.join(getbst(ltrs))

ltrs = []
for i in range(max(mdpth)):
    ltrs.append([])
getltrs(nt,0)

for i in ltrs:
    print(len(i),i)

getbst(ltrs)

ans = ans + ''.join(getbst(ltrs))
print(ans)
print(nums)

# ZGZPJLNZPZWYLXJVVG
# ZGZPJLNZPZWYLXJVVG
# UJGPVZYYLYSTWVXSWRVYLZHGLXVR
    
