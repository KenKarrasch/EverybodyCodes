q = open('day4-1in.txt').read().split('\n')
f = [int(n) for n in q]
gr = 1
for t in range(1,len(f)):
    gr *= f[t-1]/f[t]
print(gr * 2025)
