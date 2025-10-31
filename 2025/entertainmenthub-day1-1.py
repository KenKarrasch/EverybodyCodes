f = open('day1-1in.txt').read().split('\n\n')

pb = f[0].split('\n')
sq = f[1].split('\n')

tly = 0

def printslot(x,y):
    for i in range(len(pb)):
        strg = ''        
        for j in range(len(pb[i])):
            if i == y and j == x:
                strg = strg + 'o'
            else: strg = strg + pb[i][j]
        print(strg)

for i in range((int) ((len(pb[0])+1)/2)):
    x,y = 0,0
    dr = 0        
    x = i * 2
    while y < len(pb):        
        if sq[i][dr] == 'L':
            x -= 1
            if x < 0:
                x += 2
        if sq[i][dr] == 'R':
            x += 1
            if x >= len(pb[0]):
                x -= 2        
        while y < len(pb) and pb[y][x] == '.':            
            y += 1
        dr += 1
    if (((x/2) + 1) * 2) - (i + 1) > 0:
        tly += (int) ((((x/2) + 1) * 2) - (i + 1))

print(tly)
