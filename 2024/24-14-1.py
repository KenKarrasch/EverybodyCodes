f = open('24-14.txt').read().split(',')

r,c = 0,0

dr = {'U': (1,0), 'D': (-1,0), 'L': (0,-1), 'R': (0,1)}

ht = []

rv = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L' }
last = 'U'

for i in f:    
    d = i[0]
    if d == 'F':
        d = last
    if d == 'B':
        print(last)
        d = rv[last]        
    r += dr[d][0]*int(''.join(i[1:]))
    c += dr[d][1]*int(''.join(i[1:]))
    if i[0] not in 'FB':
        last = i[0]
    ht.append(r)
print(max(ht))
