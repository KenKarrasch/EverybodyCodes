# Part 1 - uses list to manage the search space. (Instead of recursion, by the input I figured it would just exceed recursion limit.

bt = [int(i) for i in open('24-9-ex2.txt').read().split('\n')]


print(bt)
bt = range(21, 60)#[18,19,18,35]
av = [1, 3, 5, 10]
av = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

tl = 0
bst = []

#bst = { 2:2, 18:2, ]


for g in bt:
    dn = False    
    cd = [[[],g]]
    bst = []
    while not dn:
        #print('cd',cd)
        if(len(cd) > 0):
            cdd = cd.pop()     
            #if(len(cd)%100 == 0):
                #print(len(cd))
            sts = cdd[0][:]
            #print('sts',sts)
            for a in av: 
                stsc = sts[:]
                #print('a',a,stsc)           
                stsc.append(a)            
                lft = cdd[1]
                if lft - a == 0:
                    #dn = True     

                    bst.append(stsc)       
                    #print('found',lft,a,stsc)
                    tl += len(stsc)
                if lft - a > 0:   
                    #print('adding',[stsc,lft-a])             
                    cd.append([stsc,lft-a])
        else: dn = True

    mn = 100000
    bstr = []
    for i in bst:
        if len(i) < mn:
            mn = len(i)
            bstr = i[:]
    print(g,mn,bstr)
#print(bst)
print(tl)

