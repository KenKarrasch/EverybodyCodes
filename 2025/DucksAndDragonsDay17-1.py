f = open('day1-1in.txt').read().split('\n')

rc = (int) (len(f[0])/2)
cc = (int) (len(f)/2)

tly = 0
lv = 10

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
   print ln
         
print tly
