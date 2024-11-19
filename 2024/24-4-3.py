f =  [int(i) for i in open('24-4-3.txt').read().split('\n')]


sweep = max(f) - min(f)

mr = 1000000000000

res = 0
dn = False
for tg in range(sweep):
    if not dn:
        dr = 0
        if tg % 10000 == 0:
            print(tg)
            if(tg != 0):
                print(res, mr)            
        sm = min(f) + tg
        for i in f:
            am = i - sm
            if am < 0:
                am = -am
            dr += am
        if dr < mr:
            mr = dr
        else: dn = True
        res = dr
print('part 3 -', mr)
