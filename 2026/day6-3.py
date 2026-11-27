import sys
f = open('day6-3.txt').read().splitlines()

ing = {}

sys.setrecursionlimit(5000)

for i in f:
    ing[i.split(':')[0]] = i.split(':')[1].split(',')

print(ing)

sl = []
nls = []

def sch(i,ind,trk,dpth):       
    print('searching',ind + i)     
    #print(dpth)   

    if i in ing.keys():        
        for t in ing[i]:     
            if t.startswith('NULL'):
                print('found')
                if t not in nls:
                    if len(nls) == 1:
                        return True
                    else:
                        nls.append(t)
            if t not in trk:                            
                ntrk = trk[:]
                ntrk.append(t)
                if sch(t,ind + ' '
                '',ntrk,dpth+1):
                    return True
    return False    

ct = 0
twoing = []
for i in ing.keys():
    print()
    nls = []
    print('Ingredient: ',i)
    if sch(i,'',[i],0):    
        print(i, ' had two or more ingredients')
        ct += 1
        twoing.append(i)

print(ct)
print(twoing)
