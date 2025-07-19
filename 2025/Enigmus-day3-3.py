import re
import copy
import math

f = open('day3-3.txt').read().split('\n')

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

snc = []

for i in range(len(con)):
    l,a = con[i][0],con[i][1]
    snc.append([mx-a,(mx-l)-a])

print('t',con)
print('snc',snc)

snc.sort()

ac = [0,1]

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def crt(a1, m1, a2, m2):
    """Solve the system t ≡ a1 mod m1, t ≡ a2 mod m2."""
    g, p, q = extended_gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None  # No solution
    lcm = m1 // g * m2
    x = (a1 + (a2 - a1) // g * p % (m2 // g) * m1)
    return x % lcm, lcm

def find_alignment(startsquare1, cyclelength1, startsquare2, cyclelength2):
    # Steps to reach last square for each system
    a1 = (cyclelength1 - startsquare1) % cyclelength1
    a2 = (cyclelength2 - startsquare2) % cyclelength2

    # Chinese remainder theorem
    # Solve t ≡ a1 mod cyclelength1, t ≡ a2 mod cyclelength2
    result = crt(a1, cyclelength1, a2, cyclelength2)
    if result is None:
        return None, None  # No alignment possible
    t, period = result
    return t, period


for i in snc[::-1]:
    fd = False    
    bt1 = [0,0]
    bt2 = [0,0]
    print('ac,i',ac,i)
    if ac[0] <= i[1]:
        bt1[0] = ac[0]
        bt1[1] = ac[1]
        bt2[0] = i[1]
        bt2[1] = i[0]
    else:
        bt1[0] = i[1]
        bt1[1] = i[0]
        bt2[0] = ac[0]
        bt2[1] = ac[1]
    day = bt1[0]    
    print('bt1,bt2',bt1,bt2)
    print(bt1[1] - bt1[0], bt1[1], bt2[1] - bt2[0], bt2[1])
    t, period = find_alignment(bt1[1] - bt1[0], bt1[1], bt2[1] - bt2[0], bt2[1])
    ac[0] = t
    ac[1] = period
    print('ac',ac)
print('Enigmatus day 3 part 3 answer:',ac[0])


# > 30860000
