fi = open('day6-3in.txt').read()
# 1, 2, skip a few, 999, 1000
print(len(fi))
ln = 10000
ds = [0]
lns = 1000
dsd = [0]
f = ''
for i in range(1000):
    f = f + fi
ltly = 0
i = 0
while i < len(f):
    tly = 0
    for j in range(i,i + lns + 1):
        if j < len(f):
            if abs(ord(f[i])-ord(f[j])) == 32:                
                tly += 1
            #if ord(f[j])-ord(f[i]) == 32:                
            #    tly += 1
    ltly += tly
    if i % ln == 0:        
        dsd.append(ltly - ds[-1])        
        ds.append(ltly)
    if i == 20000:
        i += ln*996
        ltly += 996 * dsd[-1]        
    if i % 1000 == 0:
        print(i,'of 10,000,000 (20,000 to 9,980,000 will be skipped)')
    i += 1
        
print(ltly)


# not 1662831504
# not 1661167008
# not 1664496321
# not 1664247409
