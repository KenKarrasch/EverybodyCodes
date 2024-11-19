f =  [int(i) for i in open('24-4-2.txt').read().split('\n')]

print(f)

sm = min(f)
dr = 0
for i in f:
    dr += i - sm

print(dr)

