f = open('24-12-1.txt').read().split('\n')

# Surprisingly got rank 55 opn global leaderboard

print(f)

t = []



for i in range(len(f)):
    for d in range(len(f[i])):
        if f[i][d] == 'T':
            t.append([d, -1 + len(f) - i])

print(t)

dr = [[1,1],[1,0],[1,-1]]
hts = []
rv = 0

for s in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:#range(3): # shooting power    
    for i in [3,2,1]:#[1,2,3]:  # Segment number
        p = [1,i]
        for d in [0,1,2]: #angles                  
            dist = s
            if (d == 2): # final phase unlimited
                dist = 50            
            for tr in range(dist):
                print(p)
                p = [p[0] + dr[d][0], p[1] + dr[d][1]]
                if (p in t) and (p not in hts):
                    print('hit')
                    hts.append(p)
                    rv += s*i

print('part 1 -',rv)

