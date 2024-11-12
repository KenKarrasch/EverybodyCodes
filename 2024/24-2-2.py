f = open('24-2-2.txt').read().split('\n')

words = f[0].split(':')[1].split(',')

#print(words)


ty = 0
for ln in range(len(f)-2):    
    runes = []
    runesl = []
    runic = f[ln+2]    
    #print('runic',runic)
    for w in words:
        #print('word',w)
        for l in range(1+len(runic)-len(w)):
            sct = runic[l:len(w)]
            gd = True
            for lt in range(len(w)):
                if(runic[l+lt] != w[lt]):    
                    gd = False
            if gd:
                for lt in range(len(w)):
                    if(l+lt not in runes):
                        runes.append(l+lt)
                        #runesl.append(runic[l+lt])        
                runesl.append(w)
        #runic = runic[::-1]
        for l in range(1+len(runic)-len(w)):
            sct = runic[l:len(w)]
            gd = True
            for lt in range(len(w)):
                if(runic[l+lt] != w[::-1][lt]):    
                    gd = False
            if gd:
                for lt in range(len(w)):
                    if(l+lt not in runes):
                        runes.append(l+lt)
                        #runesl.append(runic[l+lt])        
                runesl.append(w)
    #print(runes,runesl)
    #print(len(runes),len(runesl))

    ty += len(runes)

print('part 2 -',ty)

#failed attempts
#5252
#5430
#5072
# first letter is 5
