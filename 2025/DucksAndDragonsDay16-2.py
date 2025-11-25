f = [int(x) for x in open('day16-2in.txt').read().split(',')]
pm = []
for i in range(1,90):
  pr = True
  for j in range(2,i):
     if i!=j:
         if i%j == 0:
             pr = False
  if pr:
      pm.append(i)

f = [0] +f
nm = []
sz = len(f)

for i in range(len(f)):
   if i in pm:
     if f[i] > 0:
        nm.append(i)
        for w in range(sz):
          if w*i < sz:
            f[w*i] -= 1
            
for i in range(1,len(f)):
    if f[i] > 0:
      nm.append(i)
      for w in range(sz):
        if w*i < sz:
          f[w*i] -= 1
        
m = 1
for i in nm:
    m *= i

print m
