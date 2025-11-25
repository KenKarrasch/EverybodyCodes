f = [int(x) for x in open('day16-1ex1.txt').read().split(',')]

b = [0]*91
for n in range(len(f)):
  for i in range(len(b)):
    if i%f[n]==0:
       b[i] += 1

tly = 1

for i in f:
    tly *= i
    
print tly
