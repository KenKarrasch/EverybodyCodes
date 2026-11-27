f = open('day6-2.txt').read().splitlines()

ing = {}

for i in f:
    ing[i.split(':')[0]] = i.split(':')[1].split(',')

print(ing)

ings = set()
sl = []

def sch(i,ind,trk):       
    print('searching',ind + i)     
    if i in ing.keys():        
        for t in ing[i]:     
            if t == 'NULL':
                print('found')
                return True
            if t not in trk:            
                ings.add(t)
                ntrk = trk[:]
                ntrk.append(t)                
                if sch(t,ind + '    ',ntrk):
                    return True    
    return False

ct = 0
for i in ing.keys():
    ings = set()
    print()
    if sch(i,'',[i]):
        ct += 1
print(ct)
