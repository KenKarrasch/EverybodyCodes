f = open('day6-2ex1.txt').read()

tly = 0
for i in range(len(f)):
    for j in range(i+1,len(f)):
        if f[i] == 'A' and f[j] == 'a':
            tly += 1
print(tly)
