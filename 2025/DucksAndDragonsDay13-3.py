f = open("day13-3in.txt").read().split('\n')
dl = [0]*len(f)
fr = 0
for i in range(len(f)):
    if i%2==0:
      dl[(int) (i/2)] = f[i]
    else:
      dl[(int) (-i/2)] = f[i]
rf = [0]
r = 0
dl = ['1-1'] + dl
for i in dl:
    nms = [int(x) for x in i.split('-')]
    jp = abs(nms[0]-nms[1])+1
    rf.append(rf[-1]+jp)
sz = rf[-1]
rf = rf[:-1]
nr = 202520252025%sz
for i in range(len(rf)):
    if nr < rf[i]:
        d = nr - rf[i-1]
        rg = [int(x) for x in dl[i-1].split('-')]
        if i-1 <= (len(dl))/2:
            print rg[0] + d
            break
        else:
            print rg[1] - d
            break
