f =  open('24-11-2.txt').read().split('\n')

bk = {}

for i in f:
    bts = i.split(':')
    bk[bts[0]] = bts[1].split(',')

lt = ['Z']

for i in range(10):
    nlt = []
    for l in lt:
        lts = bk[l]
        for j in lts:
            nlt.append(j)
    lt = nlt[:]

print('part 2 -', len(lt))
