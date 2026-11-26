f = open('day4-1.txt').read().split('\n')

print(f)

mdr = int(len(f)/2)
mdc = int(len(f[0])/2)

ones = []
hashes = [(mdr,mdc)]
llhashes = []

dr = [(-1,-1),(-1,0),(-1,1), (0,-1),(0,1), (1,-1),(1,0),(1,1)]

nc = []

def scan(r,c):    
    for d in dr:    
        sr = (r+d[0],c+d[1])     
        if sr not in hashes:
            if sr not in llhashes:
                if (r+d[0],c+d[1]) not in nc:
                    nc.append((r+d[0],c+d[1]))    

def landlocked(r,c):        
    for d in dr:           
        sr = (r+d[0],c+d[1])     
        if sr not in hashes and sr not in llhashes :
            return False
    return True


for r in range(len(f)):
    for c in range(len(f[0])):
        if f[r][c] == '1':
            ones.append((r,c))

dn = False
llhashes = []
oldcount = 0
while oldcount != len(hashes) + len(llhashes):
    oldcount = len(hashes) + len(llhashes)
    newhashes = []
    nc = []
    for h in hashes:                
        scan(h[0],h[1])    
    for n in nc:
        ct = 0
        for d in dr:       
            sr = (n[0]+d[0],n[1]+d[1])
            if sr in ones or sr in hashes or sr in llhashes:
                ct += 1
        if ct >= 5:
            newhashes.append((n[0],n[1]))
    for i in newhashes:
        if i not in hashes:            
            hashes.append(i)
    for r in range(len(f)):
        ln = ''
        for c in range(len(f[0])):
            ch = f[r][c]
            if (r,c) in llhashes:
                ch = '_'
            if (r,c) in hashes:
                ch = '#'
            ln = ln + ch
        print(ln)

    # Cleanup
    for h in hashes:       
        if landlocked(h[0],h[1]):
            hashes.remove((h[0],h[1]))
            if h not in llhashes:
                llhashes.append((h[0],h[1]))               
    print('nc',len(nc),'hashes',len(hashes),'llhashes',len(llhashes))
print(len(hashes) + len(llhashes))
    
