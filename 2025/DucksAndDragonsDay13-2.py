f = open("day13-2in.txt").read().split('\n')
sz = 0
for i in range(len(f)):
  nms = [int(x) for x in f[i].split('-')]
  sz += 1 + nms[1] - nms[0]
dl = [0]*(sz-1)
dl = [1] + dl
fr = 0
br = 1
for i in range(len(f)):
  nms = [int(x) for x in f[i].split('-')]
  for j in range(nms[0],nms[1]+1):
    if i%2==0:
      dl[fr] = j
      fr += 1
    else:
      dl[-br] = j
      br += 1
dl =  [1] + dl
print dl[20252025%len(dl)]
