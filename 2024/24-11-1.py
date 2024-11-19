f =  open('24-11-1.txt').read().split('\n')

bk = {}

for i in f:
    bts = i.split(':')
    bk[bts[0]] = bts[1].split(',')

print(bk)

lt = ['A']

for i in range(4):
    nlt = []
    for l in lt:
        lts = bk[l]
        for j in lts:
            nlt.append(j)
    lt = nlt[:]

print('part 1 -', len(lt))
