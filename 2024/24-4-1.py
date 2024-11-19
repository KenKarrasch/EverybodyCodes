f =  [int(i) for i in open('24-4-1.txt').read().split('\n')]

sm = min(f)
dr = 0
for i in f:
    dr += i - sm

print('part 1 -',dr)
