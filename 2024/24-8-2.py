f = open('24-8-2.txt').read().split('\n')

bl = 20240000
b = 1
t  = 1
yn = int(f[0])
ly = 1
while b < bl:
    t = (t*yn)%1111
    ly += 2
    b += ly*t    

print ('part 2 -',(b-bl)*ly)
