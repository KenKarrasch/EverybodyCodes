f = open('day6-1.txt').read().splitlines()

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
            if t not in trk:            
                ings.add(t)
                ntrk = trk[:]
                ntrk.append(t)                
                sch(t,ind + '    ',ntrk)

sch('NULL','',['NULL'])    
print(ings)
print(len(ings))
