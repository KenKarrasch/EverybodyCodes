import math

f = open('in3.txt').read().split('\n')
tly = 0
for iso in f:
    n = 0
    print(iso)
    p,nm = iso.split('-')[1].split()
    onm,op = nm,p
    lnm,lp = len(nm), len(p)
    rev_s = p[::-1]
    multiplier = (lnm // len(p)) + 2
    repeated = rev_s * multiplier
    p = repeated[:lnm][::-1]
    for i in range(lnm):
        n += int(nm[i])*math.pow(int(p[i%lp]),lnm - 1 -i)
    print('old n',n)
    oldn = n 
    scan = math.pow(10,lnm)
    sc = 0
    #for i in range(int(math.pow(10,lnm-1)),int(math.pow(10,lnm))-1):
    #for i in range(1,int(math.pow(10,lnm))-1):
    for ti in range(1,int(onm)+1):
        if ti%10000 == 0:
            print('trialling', ti)
        nm = str(ti)
        n = 0
        lnm = len(nm)
        rev_s = op[::-1]
        multiplier = (lnm // len(p)) + 2
        repeated = rev_s * multiplier
        p = repeated[:lnm][::-1]
        for i in range(lnm):
            n += int(nm[i])*math.pow(int(p[i%lp]),lnm - 1 -i)
        #print('this n',ti,n)
        if n == oldn:
            if(ti == int(onm)):
            #if lnm != len(onm):
            #    print('failed')
            #else:
            #    print(i,onm)
            #    if(ti == int(onm)):
                    print('good')
                    sc = oldn
            else:
                    print('failed')
                    sc = 0
            print('n',n)
            print('found',p)
            break
    print('sc',sc)
    tly += sc
    print('tly',tly)
print('total tly',tly)

 

		
 
 
 
