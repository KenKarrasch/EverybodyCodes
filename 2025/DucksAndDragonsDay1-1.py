f = open('day1-1in.txt').read().split('\n\n')
inst = f[1].split(',')
pl = f[0].split(',')
rf = 0
for i in inst:
    if i[0] == 'R':
        rf += int(i[1])
    if i[0] == 'L':
        rf -= int(i[1])
    if rf >= len(pl):
        rf = len(pl) - 1
    if rf < 0:
        rf = 0
print(pl[rf])
