f = open('day6-2ex1.txt').read()

tly = 0
for i in range(len(f)):
    for j in range(i+1,len(f)):
        if f[i] == 'A' and f[j] == 'a':
            tly += 1
        if f[i] == 'C' and f[j] == 'c':
            tly += 1
        if f[i] == 'B' and f[j] == 'b':
            tly += 1

print(tly)
