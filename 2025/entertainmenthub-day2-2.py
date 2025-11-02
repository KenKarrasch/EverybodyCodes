f = open('day2-2in.txt').read()
ord = ['R','G','B']
bal = []
for r in range(100):
    for i in f:
        bal.append(i)
cl = 0
while len(bal) > 0:    
    bl = bal[0]
    bal = bal[1:]
    if bl == ord[cl%3]:   
        if len(bal)%2 == 1:            
            opp = (int) (len(bal)/2)
            bal = bal[0:opp] + bal[opp+1:]
    cl += 1
print(cl)
