f = open('24-8-3.txt').read().split('\n')

bl = 160 

t = 1 
yn = 2 
yn = int(f[0])  #941592

cols = [1] 
layer = 1 
fw = 1
ac = 5
ac = 10

blocks = 0
target = 125820924
target = 202400000

lyr = 0
while blocks < target:           
    t = (t*yn)%ac + ac
    layer += 1         
    ncols = [0] 
    for i in cols: 
        ncols.append(i) 
    ncols.append(0) 
    for i in range(len(ncols)): 
        ncols[i] += t     
    cols = ncols[:]     
    w = len(cols)        
    r = 0    
    for i in cols[1:-1]:
        r += ((yn * w) * i)%ac      
    blocks = sum(cols)-r               
    print(sum(cols)-r,2+lyr)
    lyr += 1

print('part 3 -',blocks - target)
