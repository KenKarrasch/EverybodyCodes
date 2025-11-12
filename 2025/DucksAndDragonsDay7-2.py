f = open('day7-2in.txt').read().split('\n\n')

nms = f[0].split(',')
rls = [y.split(' > ') for y in f[1].split('\n')]

def pok(l1,l2):    
    for i in rls:
        if l1 == i[0] and l2 in i[1]:
            return True
    return False
            
def gs(s):    
    for l in range(len(s)-1):
        if not pok(s[l],s[l+1]):
            return False
    return True

gds = []
for g in range(len(nms)):
    i = nms[g]    
    if gs(i):
        gds.append((i,g))

tly = 0
for i in gds:
    tly += i[1] + 1
print(tly)
