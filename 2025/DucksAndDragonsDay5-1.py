q = open('day5-1in.txt').read()
ns = [int(e) for e in q.split(':')[1].split(',')]
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
wd = ''
for i in fb:
    wd = wd + str(i[1])
print(wd)
