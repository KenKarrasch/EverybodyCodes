f = [int(y) for y in open("day13-1in.txt").read().split('\n')]
dl = [0]*len(f)
for i in range(len(f)):
    if i%2==0:
      dl[(int) (i/2)] = f[i]
    else:
      dl[(int) (-i/2)] = f[i]
dl = [1] + dl
print dl[2025%len(dl)]
