import math
f = open('day1-3.txt').read().split('\n')
#f = open('day1-2e1.txt').read().split('\n')
#f = open('day1-2.txt').read().split('\n')

def eni(n,exp,mod):
    r = 1
    rl = []
    seen = {}        
    cycle = -1
    ptr = 0
    adv = False
    jmpch = 0
    while ptr < exp:    
        r = (r * n) % mod
        rl.append(r)
        if r not in seen.keys():           
            seen[r] = ptr
        else:
            cycle = ptr - seen[r]        
            chk = sum(rl[seen[r]:ptr])
            if(ptr + cycle < exp):
                if(ptr > 5):
                    if(not adv):      
                        jmps = (math.floor((exp-ptr)/cycle)-1)
                        jmpch = chk * jmps
                        ptr += cycle * jmps
                        adv = True
                else: 
                    seen.clear()        
        ptr += 1
    #print(rl,jmpch)
    amt = 0 #''  
    #rl = rl[::-1]    
    for i in rl:#[0:5]:
        amt = amt + i #str(i)
    return(amt + jmpch)

print(eni(4,3000,110))


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
