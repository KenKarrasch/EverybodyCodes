f = open('day2-3in.txt').read()
# Needed to get crafty with the memory management, complexity n squared to n,  There is probably a faster way of doing it.
# Also made the mistake of using part 2's input, a la advent of code.

print('loading data')
ord = ['R','G','B']

bal = []
for r in range(100000):
    for i in f:
        bal.append(i)
cl = 0
rf = 0
lb = len(bal)
numleft = lb
rf = 0
while numleft > 0:    
    if (cl%100000==0):
        print(cl,'of',lb)
    while bal[cl + rf] == 'O':
        rf += 1    
    numleft -= 1       
    if bal[cl + rf] == ord[cl%3]:           
        if numleft%2 == 1:              
            bal[lb - (int) (numleft/2)-1] = 'O'
            numleft -= 1
    bal[cl+rf] = 'O'
    cl += 1    
print(cl)
