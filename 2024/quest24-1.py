f = open('24-1.txt').read()
pt = 0
for i in range(len(f)):
    if(f[i] == 'B'):
          pt +=1
    if(f[i] == 'C'):
          pt +=3

print('part 1',pt)

def getval(seq):
    pt = 0
    for i in range(len(seq)):
        if(seq[i] == 'B'):
            pt +=1
        if(seq[i] == 'C'):
            pt +=3
        if(seq[i] == 'D'):
            pt +=5    
    return(pt)


f2 = open('24-1-2.txt').read()
#f2 = 'AxBCDDCAxD'
pt = 0
for i in range((int) (len(f2)/2)):
    seq = f2[2*i] + f2[2*i+1]
    #print(seq)
    if('x' not in seq):
        pt += 2
    am = getval(seq)
    #print(am)
    pt += am #getval(seq)


print('part 2',pt)
          
f3 = open('24-1-3.txt').read()
#f3 = 'xBxAAABCDxCC'
pt = 0
for i in range((int) (len(f3)/3)):
    seq = f3[3*i] + f3[3*i+1] + f3[3*i+2]
    print(seq)
    xs = 0
    b = 0
    for x in range(3):
        if(seq[x] == 'x'):
            xs += 1    
    if (xs == 0): b += 6
    if (xs == 1): b += 2    
    print('b',b)
    am = getval(seq)
    print('am',am)
    pt += am + b #getval(seq)
    print('pt',pt)


print('part 3',pt)

