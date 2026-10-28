import math
f = open('day2-1test1.txt').read().split('\n')

print(f)
    
ns = []

def addn(n):
    if(n not in ns):
        ns.append(n)

def istop(n,lst):
    print(n,lst)
    for ls in lst:
        if n in ls:
            if ('>' in ls):                
                if ls[0] != n:
                    print('fail on',ls)
                    return False                
            if ('<' in ls):                
                if ls[2] != n:
                    print('fail on',ls)
                    return False
    return True         

def remn(n,lst):
    elst = []    
    for ls in lst:
        if (n not in ls):                
            elst.append(ls)
    return(elst)

for ln in f[0:1]:
    lsl = ln.split()
    for ls in lsl:      
        if ('>' in ls):            
            addn(ls.split('>')[0])
            addn(ls.split('>')[1])
        if ('<' in ls):
            addn(ls.split('<')[0])
            addn(ls.split('<')[1])
    print(ns)
    lsle = lsl[:]
    dn = False
    ans = ''    
    while not dn:
        for n in ns:            
            print('candidate n',n)
            if istop(n,lsle):
                print('found top',n)
                lsle = remn(n,lsle)
                print('lsle',lsle)
                ans = ans + n
                print('next', n)
        dn = True
    print(ans)


