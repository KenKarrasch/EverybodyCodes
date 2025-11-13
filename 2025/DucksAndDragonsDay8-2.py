f = [int(y) for y in open('day8-2in.txt').read().split(',')]

l = max(f) 
tly = 0

for i in range(len(f)-1):
    for j in range(i,len(f)-1):
        a = min([f[i],f[i+1]])
        b = max([f[i],f[i+1]])
        c = min([f[j],f[j+1]])
        d = max([f[j],f[j+1]])
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
print(tly)
