f = [int(y) for y in open('day8-3in.txt').read().split(',')]

l = max(f) 
bst = 0

for s in range(1,l):
    print(s)
    for e in range(s+1,l):
        tly = 0                
        for j in range(len(f)-1):
            a = min([s,e])
            b = max([s,e])
            c = min([f[j],f[j+1]])
            d = max([f[j],f[j+1]])
            if a == c and b == d:
                tly += 1
            offset = min([a,b])
            a = a - offset
            b = b - offset
            c = c - offset
            d = d - offset
            c = (c + 2 * l) % l
            d = (d + 2 * l) % l               
            if len(set([a,b,c,d])) > 3:        
                if c > b:
                    if d < b:                
                        tly += 1
                if c < b:
                    if d > b:
                        tly += 1
        if tly > bst:
            print(s,e, tly)
        bst = max(tly,bst)
print(bst)
