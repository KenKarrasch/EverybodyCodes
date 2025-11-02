f = open('day2-1in.txt').read()
ord = ['R','G','B']
bal = []
for i in f:
    bal.append(i)
bal.append('F')
cl = 0
offset = 1
while not bal[0] == 'F':      
    if bal[0] != ord[cl%3]:
        bal = bal[1:]
        cl += 1
        if bal[0] == 'F':
            offset = 0
    else:
        bal = bal[1:]
print(cl + offset)
