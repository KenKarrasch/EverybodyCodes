
def dopart(target, filename):
    f = open(filename).read().split('\n\n')
    key,gd = f[0], [[j for j in i] for i in f[1].split('\n')]
    R, C = len(gd), len(gd[0])

    e = [(-1,-1), (-1, 0), (-1, 1), ( 0, 1), ( 1, 1), ( 1, 0), ( 1,-1), ( 0,-1)]
    d = {'L': 1,'R': -1}

    def rotate(r,c,dr):    
        tmp = []
        for i in range(8):                
            tmp.append(gdt[r+e[(i+d[dr])%8][0]][c+e[(i+d[dr])%8][1]])    
        for i in range(8):                
            gdt[r+e[i%8][0]][c+e[i%8][1]] = tmp[i]
            
    def work():
        p = 0    
        for r in range(1,len(gd)-1):        
            for c in range(1,len(gd[0])-1):            
                rotate(r,c,key[p%len(key)])        
                p += 1    

    gdt = [[(i,j) for j in range(C)] for i in range(R)]

    # Make a refence book (bk) of where the letters end after on round
    bkofbk, bk = [], {}    
    work()    
    for nr,i in enumerate(gdt):
        for nc,j in enumerate(i):
            bk[(nr,nc)] = (gdt[nr][nc])
    bkofbk.append(bk)

    bt = str(bin(target)[2:])[::-1]

    # Make a book of books (bkofbk), for advancing 1,2,4,8,16,... rounds etc    
    for i in bt: 
        nbk = {}
        for k,v in bk.items(): nbk[k] = bk[v]
        bk = nbk
        bkofbk.append(nbk)

    # after converting number of rounds to binary, for each one we choose which of the bkofbks to advance. 
    # e.g. 11 decimal rounds = 1011 (binary), so advance 1,2, and 8 rounds (to advance equivalent of 11 rounds)
    for n,l in enumerate([l for l in bt]):
        ogd = [[j for j in i[:]] for i in gd]
        if l == '1':
            for r in range(R):
                for c in range(C):
                    wtg = bkofbk[n][(r,c)]                
                    gd[r][c] = ogd[wtg[0]][wtg[1]]            

    for i in gd: print(''.join(i))

dopart(1,'24-19-1.txt')
dopart(100,'24-19-2.txt')
dopart(1048576000 ,'24-19-3.txt')
