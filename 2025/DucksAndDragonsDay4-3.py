q = open('day4-3in.txt').read().split('\n')
f = [[int(g) for g in n.split('|')] for n in q[1:-1]]
f = [[1,int(q[0])]] + f
f = f + [[int(q[-1]),1]]
gr = 1
for t in range(len(f)):
    gr *= f[t][1]
    gr *= 1/f[t][0]
print((int) (gr * 100))
