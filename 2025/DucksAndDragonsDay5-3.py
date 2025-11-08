qs = open('day5-3in.txt').read().split('\n')
wds = []
ids = []
for q in qs:
    ns = [int(e) for e in q.split(':')[1].split(',')]
    ids.append(int(q.split(':')[0]))
    fb = [[-1,-1,-1]]
    for n in ns:
        dn = False    
        for i in range(len(fb)):
            if not dn:
                if fb[i][1] == -1:
                    fb[i][1] = n
                    dn = True
                newline = False
                if n > fb[i][1]:
                    if fb[i][2] == -1:
                        fb[i][2] = n
                        dn = True
                    else: 
                        if i == len(fb) - 1:
                            newline = True
                if n < fb[i][1]:
                    if fb[i][0] == -1:
                        fb[i][0] = n
                        dn = True
                    else: 
                        if i == len(fb) - 1:
                            newline = True
                if newline:
                    fb.append([-1,n,-1])
                    dn = True
        if not dn:
            fb.append([-1,n,-1])                    
    wd = ''
    wds.append(fb)
cat = []
for w in range(len(wds)):    
    wd = ''
    for f in wds[w]:        
        wd = wd + str(f[1])
    spine = [int(wd)]    
    bhs = []
    for f in wds[w]:
        lnw = ''
        for el in f:
            if el != -1:
                lnw = lnw + str(el)
        spine.append(int(lnw))
    spine.append(ids[w])    
    cat.append(spine)
cat.sort(reverse = True)
sm = 0
for i in range(len(cat)):
    sm += (i+1) * cat[i][-1]
print(sm)
