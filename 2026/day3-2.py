import math

f = open('in2.txt').read().split('\n')

tly = 0
for iso in f:
    print(iso)
    
    n = 0
    p,nm = iso.split('-')[1].split()
    lnm = len(nm)
    lp = len(p)
    ps = ''
    rev_s = p[::-1]
    multiplier = (lnm // len(p)) + 2
    repeated = rev_s * multiplier
    ps = repeated[:lnm][::-1]
    #print('ps',ps)
    p = ps
    for i in range(lnm):
        #print(int(nm[i]))
        #print(int(p[i%lp]))
        bt = int(nm[i])*math.pow(int(p[i%lp]),lnm - 1 -i)
        n += bt
        #print('bt',bt)
    print('n',n)
    tly += n
print('tly',tly)

