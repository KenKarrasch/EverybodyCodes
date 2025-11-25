f = [int(x) for x in open('day16-3in.txt').read().split(',')]
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

pw = 1

def gb(wl):
  mc = 0
  for n in nm:
    mc += (int) (wl/n)
  return(mc)
  
tg = 202520252025000

def cv(sli):
  nm = 0
  od = 1
  for i in sli[::-1]:
    nm += i*od
    od *= 10
  return nm

fd = False
pws = 0
while not fd:
  if gb(pw)>tg:
    fd = True
  else:
    pw *= 10
    pws += 1

sl = [0]*(pws+1)
dg = 0
dn = False
bst = 0
while not dn:
  nd = False
  for i in range(11):
   if not nd:
    sl[dg] = i
    if gb(cv(sl)) >= tg:
        sl[dg] -= 1
        dg += 1
        nd = True
        bst = cv(sl)
    if dg >= len(sl):
        dn = True

print bst
