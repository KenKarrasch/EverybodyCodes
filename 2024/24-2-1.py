f = open('24-2-ex1.txt').read().split('\n')

words = f[0].split(':')[1].split(',')

#print(words)

ty = 0
for w in words:
    for ln in range(len(f)-2):
        runic = f[ln+2]    
        #print('runic',runic)
        for l in range(len(runic)-len(w)):
            sct = runic[l:len(w)]
            gd = True
            for lt in range(len(w)):
                if(runic[l+lt] != w[lt]):    
                    gd = False
            if gd:
                ty += 1

        #print(ty)
print('part 1 -',ty)
