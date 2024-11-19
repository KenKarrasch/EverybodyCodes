f =  open('24-11-3.txt').read().split('\n')

# Used a dictionary to keep track of the generations of termites.  Started late, slept in with Covid, Managed to get 78th rank on Global Leaderboard.

bk = {}

for i in f:
    bts = i.split(':')
    bk[bts[0]] = bts[1].split(',')

bok = {}

for ky in bk.keys():
    bok[(ky,0)] = 1

for d in range(1,21):
    for ky in bk.keys():
        tot = 0
        for l in bk[ky]:
            if (l,d-1) in bok.keys():
                tot += bok[(l,d-1)]
            else: tot += 1
        bok[(ky,d)] = tot

bgs = []

for ky in bok.keys():
    if ky[1] == 20:
       bgs.append(bok[ky])

print('part 3 -', max(bgs)-min(bgs))
