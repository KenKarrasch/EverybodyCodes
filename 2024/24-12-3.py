f = open('24-12-3.txt').read().split('\n')

# Scored rank 91 on global rank

# Solution uses fuzzy logic to hone in on the answer, it is very slow. Could be refined signficantly


to = []
h = []

for m in f:
    cd = [int(i) for i in m.split()]
    to.append([cd[0]+1,cd[1]+1])

dr = [[1,1],[1,0],[1,-1]]

rv = 0
metnum = 0
anws = []
for m in to[5::]:
    metnum += 1
    t = [m[:]]
    print()
    print('meteor',t[0][0]-1,t[0][1]-1,'num',metnum)
    htscore = 10000000   
    met = t[0][:]
    hts = []    
    dly = 0
    if met[0]%2 == 0: 
        dly = 1
    print(dly,met[0])
    if True:
    #for dly in [0,1,2,3,4,5]:#range(0,m[1]):# time delay    
        #print()          
        #print('delay',dly)
        projectileOverMeteor = False         
        for sn in [3,2,1]:#[1,2,3]:  # Segment number
            #print()
            #print('height',sn)                        
            projectileHitatShootingPower = False 
            sp = 0
            hit = False
            #print((met[0]-met[1])//3)
            while not hit and sp < 7300//3:
            #for sp in range(1,7300): # shooting power                                 
                sp += 1
                if not projectileOverMeteor and not projectileHitatShootingPower:
                    #print('shooting power',sp)                 
                    met = t[0][:]
                    met[0] -= dly
                    met[1] -= dly   
                    p = [1,sn]

                    #hit = False
                    meteorUnderground = False
                    projectileUnderground = False
                    projectileHigherThanMeteor = False
                    passedEachOther = False
                    differentAltitudesFalling = False
                    for d in [0,1,2]: #phases - up, level, falling   
                        #print('phase',d) 
                        dist = sp
                        if (d == 2): # final phase unlimited
                            dist = 7300       
                        for tr in range(dist):   
                            if not hit and not meteorUnderground and not projectileHigherThanMeteor:
                                if not passedEachOther and not differentAltitudesFalling and not projectileUnderground:     
                                    p = [p[0] + dr[d][0], p[1] + dr[d][1]]
                                    met[0] -= 1
                                    met[1] -= 1                        
                                    #print(p,met)#,'shooting power', sp,'height', sn,'delay',dly)
                                    if (p[0] == met[0]):
                                        #print('hp',p[1],'hm',met[1])
                                        if met[1] - p[1] > 10:
                                            sp += 10
                                    if (p[0] == met[0]) and (p[1] == met[1]):
                                        print('hit',p,'shooting power', sp,'height', sn,'delay',dly)                                                
                                        hts.append([p[1],sp*sn])
                                        hit = True
                                        #projectileHitatShootingPower = True
                                    if p[1] < 1:  # Projectile above ground
                                        projectileUnderground = True
                                        if met[1] > 30:
                                            #print('us boost')
                                            sp += 10
                                    if met[1] < 1: # Meteor above ground
                                        meteorUnderground = True
                                    if p[0] > met[0]: # Projectile not overshot/passed meteor    
                                        passedEachOther = True
                                    if p[1] > met[1]: # Projectile is higher than the meteor already     
                                        projectileHigherThanMeteor = True
                                    if (d == 2) and p[1] != met[1]: # falling phase but different heights 
                                        differentAltitudesFalling = True
                                        if met[1] - p[1] > 30:
                                            #print('d2 boost',met[1], p[1])                                        
                                            sp += 10
                                    #if (d == 2) and p[1] > met[1]: # projectile Over Meteor - ie dont bother increasing shooting power
                                        #projectileOverMeteor = True
                                    #if (d == 1) and p[1] > met[1]: # projectile Over Meteor - ie dont bother increasing shooting power
                                        #67projectileOverMeteor = True
    
    #print('hts',hts) 
    lst = 1000000
    for i in hts:        
        if i[1] < lst:
            lst = i[1]
    print(lst)
    anws.append(lst)
    rv += lst

print(anws)
print('part 3 -',rv)
