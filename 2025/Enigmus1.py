import math
f = open('day1-1.txt').read().split('\n')

def eni(n,exp,mod):
    r = 1
    rl = []
    for i in range(exp):
        r = (r * n) % mod
        rl.append(r)
    amt = ''
    for i in rl[::-1]:
        amt = amt + str(i)
    return(int(amt))

print('test',eni(3,5,16))
res = []
for i in f:        
    vs = [y.split('=') for y in i.split()]
    nvs = [int(n[1]) for n in vs]    
    amt = eni(nvs[0],nvs[3],nvs[-1]) + eni(nvs[1],nvs[4],nvs[-1]) + eni(nvs[2],nvs[5],nvs[-1])    
    res.append(amt)
print(max(res))
