f = open('24-2-3.txt').read().split('\n')

words = f[0].split(':')[1].split(',')

#print(words)

grd = []
tkn = []
for ln in range(2,len(f)):
    gl = []
    tk = []
    for l in f[ln]:
        gl.append(l)
        tk.append(0)
    grd.append(gl)
    tkn.append(tk)

drs = [[0,1],[0,-1],[1,0],[-1,0]]
#print(grd)
li = len(grd)
lj = len(grd[0])
#print('li,lj',li,lj)
for w in words:        
    #print(w)
    for i in range(li):        
        for j in range(lj):            
            #print(i,j,grd[i][j])
            for d in drs:
                fd = True
                for lc in range(len(w)):
                    #print('lc',lc)
                    ic = (i+d[0]*lc)#%li
                    jc = (lj+j+d[1]*lc)%lj
                    if (ic > -1) and (ic < li):
                    #print('icjc',ic,jc)
                    #print('grd[ic][jc]',grd[ic][jc])
                        if(grd[ic][jc] != w[lc]):
                            fd = False            
                    else: fd = False          
                if fd:
                    #print(fd,d,i,j)
                    for lc in range(len(w)):
                        ic = (i+d[0]*lc)#%li
                        jc = (lj+j+d[1]*lc)%lj
                        tkn[ic][jc] = 1
                #print('dr done',d)

#print(tkn)
ty = 0
for i in range(li):
    for j in range(lj):
      if tkn[i][j]: 
        ty += 1  

print(ty)
