import itertools
f = open('day2-1.txt').read().split('\n')
   
ns = []

def addn(n):
    if(n not in ns):
        ns.append(n)

tly = 0
for ln in f:
    lsl = ln.split()
    for ls in lsl:      
        if ('>' in ls):            
            addn(ls.split('>')[0])
            addn(ls.split('>')[1])
        if ('<' in ls):
            addn(ls.split('<')[0])
            addn(ls.split('<')[1])    
    lsle = lsl[:]
    dn = False
    all_perms = itertools.permutations(ns)    
    for p in all_perms:
        st = {}
        for i in range(len(p)):
            st[p[i]] = i
        #print(st)
        gd = True
        for ls in lsl:
            #print(ls[1])
            if ls[1] == '>':
                if st[ls[0]] > st[ls[2]]:
                    gd = False                
            if ls[1] == '<':
                if st[ls[0]] < st[ls[2]]:
                    gd = False
        if gd:
            print(p)
            gr = ''
            for g in p:
                gr = gr + g
            tly += int(gr)
print(tly)


                         
    


