f = open('day1-2in.txt').read().split('\n\n')

pb = f[0].split('\n')
sq = f[1].split('\n')

tly = 0

for si in range(len(sq)):
    scores = []
    for i in range((int) ((len(pb[0])+1)/2)):
        x,y = 0,0
        dr = 0        
        x = i * 2
        while y < len(pb):        
            if sq[si][dr] == 'L':
                x -= 1
                if x < 0:
                    x += 2
            if sq[si][dr] == 'R':
                x += 1
                if x >= len(pb[0]):
                    x -= 2        
            while y < len(pb) and pb[y][x] == '.':            
                y += 1
            dr += 1
        if (((x/2) + 1) * 2) - (i + 1) > 0:
            scores.append((int) ((((x/2) + 1) * 2) - (i + 1)))    
    tly += max(scores)
print(tly)
