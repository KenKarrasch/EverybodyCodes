with open('day5-3.txt') as file:
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

sand = set()
for r in range(len(f)):
    ln = ''
    for c in range(len(f[0])):
        ch = '.'#f[r][c]
        if (r,c) in llhashes:
            ch = '_'
            sand.add((r,c))
        if (r,c) in hashes:
            ch = '#'
            sand.add((r,c))
        if (r,c) in hashes and (r,c) in llhashes:
            print('fault')
        ln = ln + ch
    print(ln)
print()


print(len(sand))

print(len(land))

nland = set()

for l in land:
    if l not in sand:
        nland.add(l)


trees = set()
for l in nland:
    tree = True
    for dr in [-2,-1,0,1,2]:
        for dc in [-2,-1,0,1,2]:
            if not (abs(dr) == 2 and abs(dc) == 2) and not (dr == 0 and dc == 0):
                if (l[0]+dr,l[1]+dc) not in nland:
                    tree = False
    if tree:
        trees.add(l)

print(trees)
for r in range(len(f)):
    ln = ''
    for c in range(len(f[0])):
        ch = '.'#f[r][c]
        if (r,c) in nland:
            ch = '#'
        if (r,c) in trees:
            ch = '@'
        #if (r,c) in sand:
        #    ch = '='
        ln = ln + ch
    print(ln) 
print()

dr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

print(list(trees).sort())
print(trees)
newtrees = set()
for i in [1,2]:
    newtrees.clear()
    for t in trees:    
        for r,c in dr:
            cr, cc = r+t[0], c+t[1]
            if (cr,cc) not in trees:                
                #print('considering',cr,cc)
                ct = 0
                for nr,nc in dr:
                    if (cr+nr, cc+nc) in trees:
                        print(ct)
                        ct += 1
                if ct >= 4:
                    #print('adding',cr,cc)
                    newtrees.add((cr,cc))
    print('newtrees',newtrees)
    trees.update(newtrees)

    print(trees)
    for r in range(len(f)):
        ln = ''
        for c in range(len(f[0])):
            ch = '.'#f[r][c]
            if (r,c) in nland:
                ch = '#'
            if (r,c) in trees:
                ch = '@'
            #if (r,c) in sand:
            #    ch = '='
            ln = ln + ch
        print(ln) 
    print()
print(len(trees))
