with open('day5-2.txt') as file:
    f = file.read().splitlines()

mdr = len(f) // 2
mdc = len(f[0]) // 2

# Use sets for O(1) instant lookups instead of lists
ones = {(r, c) for r in range(len(f)) for c in range(len(f[0])) if f[r][c] == '1'}
hashes = {(mdr, mdc)}
llhashes = set()

dr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def landlocked(r, c):
    # Check if all 8 neighbors are already processed
    return all((r + d[0], c + d[1]) in hashes or (r + d[0], c + d[1]) in llhashes for d in dr)

oldcount = 0
oldllhash = set()
while oldcount != len(hashes) + len(llhashes):
    oldcount = len(hashes) + len(llhashes)
    
    # 1. Gather unique candidate neighbors using a set
    nc = set()
    for r, c in hashes:
        for d0, d1 in dr:
            sr = (r + d0, c + d1)
            if sr not in hashes and sr not in llhashes:
                nc.add(sr)
                
    # 2. Check neighbor counts
    newhashes = set()
    for r, c in nc:
        ct = sum(1 for d0, d1 in dr if (r + d0, c + d1) in ones or (r + d0, c + d1) in hashes or (r + d0, c + d1) in llhashes)
        if ct >= 5:
            newhashes.add((r, c))
            
    hashes.update(newhashes)
    
    # 3. Cleanup safely without mutating the set during iteration
    newly_landlocked = {h for h in hashes if landlocked(h[0], h[1])}
    hashes -= newly_landlocked
    llhashes.update(newly_landlocked)



    for r in range(len(f)):
        ln = ''
        for c in range(len(f[0])):
            ch = f[r][c]
            if (r,c) in llhashes:
                ch = '_'
            if (r,c) in hashes:
                ch = '#'
            ln = ln + ch
        #print(ln)
    #print()

land = set()

for i in hashes:
    land.add(i)
for i in llhashes:
    land.add(i)    

llhashes.clear()

for r in range(len(f)):
        ln = ''
        for c in range(len(f[0])):
            ch = '.'#f[r][c]
            if (r,c) in land:
                ch = '='
            if (r,c) in hashes:
                ch = '#'
            ln = ln + ch
        print(ln)
print()




while oldcount != len(hashes) + len(llhashes):
    oldcount = len(hashes) + len(llhashes)
#for bc in range(3):

    # 1. Gather unique candidate neighbors using a set
    nc = set()
    for r, c in hashes:
        for d0, d1 in dr:
            sr = (r + d0, c + d1)
            if sr not in hashes and sr not in llhashes:
                nc.add(sr)
                
    # 2. Check neighbor counts
    newhashes = set()
    for r, c in nc:
        ct = sum(1 for d0, d1 in dr if (r + d0, c + d1) in hashes or (r + d0, c + d1) in hashes)
        if ct >= 5:
            newhashes.add((r, c))
            
    hashes.update(newhashes)
    
    # 3. Cleanup safely without mutating the set during iteration
    newly_landlocked = {h for h in hashes if landlocked(h[0], h[1])}
    hashes -= newly_landlocked
    llhashes.update(newly_landlocked)

    if False:
       for r in range(len(f)):
        ln = ''
        for c in range(len(f[0])):
            ch = '.'#f[r][c]
            if (r,c) in llhashes:
                ch = '_'
            if (r,c) in hashes:
                ch = '#'
            if (r,c) in hashes and (r,c) in llhashes:
                print('fault')
            ln = ln + ch
        print(ln)
       print()


print(len(hashes) + len(llhashes))
