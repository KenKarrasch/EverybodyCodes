f = [[x for x in i] for i in open('day20-1in.txt').read().split('\n')]

tly = 0

for ln in range(len(f)-1):    
    for i in range(len(f[ln])-1):        
        if f[ln][i] == 'T':
            if f[ln][i+1] == 'T':                
                tly += 1

for ln in range(len(f)-1):    
    for i in range(len(f[ln])-1):
        if((1+i+ln)%2 == 0):
            if f[ln][i] == 'T':
                if f[ln+1][i] == 'T':
                    tly += 1

print(tly)
