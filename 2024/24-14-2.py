fn = open('24-14-2.txt').read().split('\n')

r,c = 0,0

dr = {'U': (1,0,0), 'D': (-1,0,0), 'L': (0,-1,0), 'R': (0,1,0),'F': (0,0,1), 'B': (0,0,-1)}

ht = []

sgs = []

last = 'U'
for b in fn:
    f = b.split(',')
    r,c,z = 0,0,0
    for i in f:    
        print(i)
        d = i[0]        
        for s in range(int(''.join(i[1:]))):
            r += dr[d][0]            
            if (r,c,z) not in sgs:
                sgs.append((r,c,z))
        for s in range(int(''.join(i[1:]))):
            c += dr[d][1]            
            if (r,c,z) not in sgs:
                sgs.append((r,c,z))        
        for s in range(int(''.join(i[1:]))):
            z += dr[d][2]            
            if (r,c,z) not in sgs:
                sgs.append((r,c,z))   
        ht.append(r)
        print(len(sgs),r,c,z)
    print()
