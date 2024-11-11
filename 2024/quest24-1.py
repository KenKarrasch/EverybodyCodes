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
    for i in [0,1]:
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
