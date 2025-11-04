f = open('day1-2in.txt').read().split('\n\n')

inst = f[1].split(',')
pl = f[0].split(',')
rf = 0
for i in inst:
    digits = ""
    for char in i:
        if char.isdigit():
            digits += char
    number = int(digits)
    if i[0] == 'R':
        rf += int(digits)
    if i[0] == 'L':
        rf -= int(digits)
    rf = rf % len(pl)

print(pl[rf])
