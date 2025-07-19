import re

f = open('day3-1.txt').read().split('\n')

print(f)

con = []
mx = 0
steps = 100

def tfm(x,y,mx):
    lvl = mx - (y + x - 1) # bottom level is 0
    alg = x
    return (lvl,alg)

def itfm(a,l,mx):
    print('l,a',l,a)
    y = (mx - l) - (a - 1)
    x = a    
    print('x,y',x,y)
    return (x,y)

for i in f:
    ns = [int(x) for x in re.findall(r'\d+', i)]
    mx = max(mx,ns[1]+ns[0])
    con.append(ns)

print(con)

for i in range(len(con)):
    l,a = tfm(con[i][0],con[i][1],mx)    
    con[i][0] = a
    con[i][1] = l

print(con)

for i in range(len(con)):
    con[i][0] = 1 + (con[i][0]-1+steps)%(mx-con[i][1])

tly = 0

for i in range(len(con)):
    x,y = itfm(con[i][0],con[i][1],mx)
    con[i][0] = x
    con[i][1] = y
    tly += x + (100 * y)
print(con)
print(tly)
