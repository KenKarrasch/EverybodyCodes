

f = [[int(x) for x in i.split()] for i in open('24-5-1.txt').read().split('\n')]

ff = []
for i in range(len(f[0])):
    r = []
    for j in range(len(f)):
        r.append(f[j][i])
    ff.append(r[:])
    print(r)
print(f)
print(ff)

i = 0
dn = False

for c in range(10):
#while not dn:
    n = ff[i][0]  # the number
    #print('n',n)
    nl = (i+1)%4  # next line moded
    #print('nl',nl)
    l = len(ff[nl]) # length of the next line
    #print('l',l)
    if ((n-1)//l)%2 == 0:  # going down (may have gone down & up already)        
        
        # n-1//l       0,0,0,     1,1,1,      0,0,0
        # ex len 3, dn 1,2,3,  up 4,5,6, dn , 7,8,9
        #print('down')
        el = n%l
        ff[i] = ff[i][1:][:]
        ff[nl] = ff[nl][:el-1][:] + [n] + ff[nl][el-1:][:]
    else:  # going up
        # el           0,0,0,     1,1,1,      0,0,0
        # ex len 3, dn 1,2,3,  up 4,5,6, dn , 7,8,9        
        #print('up')
        el = n%l
        ff[i] = ff[i][1:][:]
        ff[nl] = ff[nl][:1+l-el][:] + [n] + ff[nl][1+l-el:][:]
    i += 1
    i = i%4
    #print(ff)
    #if(i == 3): dn = True
    ans = []    
    for y in ff:
        ans.append(y[0])
    #print(ans)
    print(''.join([str(le) for le in ans]))
