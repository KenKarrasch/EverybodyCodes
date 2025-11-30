f = open('day17-2in.txt').read().split('\n')

rc = (int) (len(f[0])/2)
cc = (int) (len(f)/2)

tly = 0
lv = 10

ch = []

for rd in range(50):
  lv = rd
  tly = 0
  for r in range(len(f)):
   ln = ''
   for c in range(len(f[r])):
     dr = r-rc
     dc = c-cc
     if (dr*dr) + (dc*dc) <= lv*lv:
         ln = ln + f[r][c]
         if f[r][c] != '@':
          tly += int(f[r][c])
     else:
       ln = ln + ' '
  ch.append(tly)
         
scs = []
bst = 0
bsti = 0

for i in range(len(ch)-1):
    scs.append((ch[i+1]-ch[i])*(i+1))
    if ch[i+1]-ch[i] > bst:
        bst = ch[i+1]-ch[i]
        bsti = i
        
print scs[bsti]
