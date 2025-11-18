f = [int(y) for y in open('day11-2in.txt').read().split('\n')]
ch = True
rd = 0
while ch:
    ch = False
    for r in range(len(f)-1):
        if f[r] > f[r+1]:
            f[r+1] += 1
            f[r] -= 1
            ch = True
    rd += 1

ch = True
while ch:
    ch = False
    for r in range(1,len(f))[::1]:
        if f[r] > f[r-1]:
            f[r-1] += 1
            f[r] -= 1
            ch = True
    rd += 1
    if ch %10000 == 0:
        print ch
    
tly = 0
for i in range(len(f)):
    tly += (i+1)*f[i]
    
print rd -2
