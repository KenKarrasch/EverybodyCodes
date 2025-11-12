f = open('day7-1in.txt').read().split('\n\n')

nms = f[0].split(',')
rls = [y.split(' > ') for y in f[1].split('\n')]

def pok(l1,l2):    
    for i in rls:
        if l1 == i[0] and l2 in i[1]:
            return True
    return False
            

for i in nms:
    ok = True
    for l in range(len(i)-1):
        if not pok(i[l],i[l+1]):
            ok = False
    if ok:
        print(i)
