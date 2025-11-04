f = open('day1-3in.txt').read().split('\n\n')

inst = f[1].split(',')
pl = f[0].split(',')

rf = 0

def swap(rf):
    tmp = pl[rf]
    pl[rf] = pl[0]
    pl[0] = tmp

for i in inst:
    digits = ""
    for char in i:
        if char.isdigit():
            digits += char
    number = int(digits)    
    if i[0] == 'R':
        rf = int(digits)
    if i[0] == 'L':
        rf = -int(digits)
    rf = rf % len(pl)
    swap(rf)    

print(pl[0])
    
