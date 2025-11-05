f = open('day2-3in.txt').read()

x = int(f.split('[')[1].split(',')[0])
y = int(f.split(',')[1].split(']')[0])

A = [x,y]

gr = []
rg = 1000
for j in range(rg+1):
    ln = []
    for i in range(rg+1):
        ln.append([A[0] + (int) (i*1000/rg), A[1] + (int) (j*1000/rg)])
    gr.append(ln)

def add(X1,Y1,X2,Y2):
    return([X1 + X2, Y1 + Y2])

def mult(X1,Y1,X2,Y2):
    return([X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2])

def div(X1,Y1,X2,Y2):   
    lim = 10000000000000000000
    if lim < X1:            
        return [-10000000000,-10000000000]
    if lim < X2:        
        return [-10000000000,-10000000000]
    if lim < Y1:        
        return [-10000000000,-10000000000]
    if lim < Y2:        
        return [-10000000000,-10000000000]
    if -lim > X1:            
        return [-10000000000,-10000000000]
    if -lim > X2:        
        return [-10000000000,-10000000000]
    if -lim > Y1:        
        return [-10000000000,-10000000000]
    if -lim > Y2:        
        return [-10000000000,-10000000000]
    return([int(X1 / X2),int(Y1 / Y2)])

eng = []

for j in range(rg+1):
  print(j,'of 1000')
  for i in range(rg+1):        
        p = [0,0]
        A = [gr[i][j][0],gr[i][j][1]]   
        done = False
        for c in range(100):
            if not done:
                p = mult(p[0],p[1],p[0],p[1])
                p = div(p[0],p[1],100000,100000)
                if p != [-10000000000,-10000000000]:
                    p = add(p[0],p[1],A[0],A[1])            
                else: done = True
        if (-1000000 < p[0] < 1000000) and (-1000000 < p[1] < 1000000):
            eng.append(p)
        else:
            done = True        
print(len(eng))
