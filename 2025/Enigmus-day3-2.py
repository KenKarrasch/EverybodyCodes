import re
import copy

f = open('day3-2.txt').read().split('\n')

print(f)

con = []
mx = 0
steps = 100

def tfm(x,y,mx):
    lvl = mx - (y + x - 1) # bottom level is 0
    alg = x
    return (lvl,alg)

def itfm(a,l,mx):    
    y = (mx - l) - (a - 1)
    x = a        
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

consv = copy.deepcopy(con)

gd = False
day = 0
while not gd:    
    gd = True
    con = copy.deepcopy(consv)
    for i in range(len(con)):
        con[i][0] = 1 + (con[i][0]-1+day)%(mx-con[i][1])
    for i in range(len(con)):
        x,y = itfm(con[i][0],con[i][1],mx)    
        con[i][0] = x
        con[i][1] = y        
        if y != 1:   
             gd = False
    day += 1
    if day% 1000 == 0:
        print(day)
print(con,day-1)
