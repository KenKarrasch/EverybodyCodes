f = open('24-8-1.txt').read().split('\n')

bl = int(f[0])
#bl = 13

h = 1
bs = 1
b = h

while b < bl:
    h += 1
    b = h*h
    bs += 2

print ('part 1 -',(b-bl)*bs)
