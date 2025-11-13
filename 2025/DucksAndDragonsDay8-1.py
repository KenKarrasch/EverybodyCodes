f = [int(y) for y in open('day8-1in.txt').read().split(',')]

l = max(f)/2 
tly = 0

for i in range(len(f)-1):
    if f[i] - f[i+1] == l:      
        tly += 1
    if f[i] - f[i+1] == -l:
        tly += 1
print(tly)
