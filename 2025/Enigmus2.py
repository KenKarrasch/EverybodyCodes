import math
f = open('day1-2.txt').read().split('\n')
#f = open('day1-2e1.txt').read().split('\n')
#f = open('day1-2.txt').read().split('\n')

def eni(n,exp,mod):
    #print(n,exp,mod)
    r = 1
    rl = []
    seen = {}        
    cycle = -1
    ptr = 0
    adv = False
    while ptr < exp:    
        r = (r * n) % mod
        rl.append(r)
        if r not in seen.keys():           
            seen[r] = ptr
        else:
            cycle = ptr - seen[r]                                    
            if(ptr + cycle < exp):
                if(ptr > 5):
                    if(not adv):                        
                        ptr += cycle * (math.floor((exp-ptr)/cycle)-1)
                        adv = True
                else: 
                    seen.clear()        
        ptr += 1
        #print(r,ptr)

    amt = ''    
    rl = rl[::-1]
    #print(rl)
    for i in rl[0:5]:
        amt = amt + str(i)
    return(int(amt))

#print(eni(6,18,14))


res = []
amt = []
#if False:
for i in f:          
    vs = [y.split('=') for y in i.split()]
    nvs = [int(n[1]) for n in vs]    
    amt.append(eni(nvs[0],nvs[3],nvs[-1]))
    amt.append(eni(nvs[1],nvs[4],nvs[-1]))
    amt.append(eni(nvs[2],nvs[5],nvs[-1]))
    res.append(sum(amt))
    print(amt)
    amt = []

print(max(res))

#164051258244321 - Your answer length is: correct, The first character of your answer is: correct

#1507702060886 
#1507702060886
