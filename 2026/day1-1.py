import math
f = [int(x) for x in open('day1-1.txt').read().split(',')]
tly = 0
for i in f:    
    base = math.floor(math.sqrt(i))
    if(base*base != i):
        base += 1
    nsq = base*base
    np = base*base - i
    tly += np
print('tly',tly)
