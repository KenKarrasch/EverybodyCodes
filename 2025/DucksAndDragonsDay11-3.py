f = [int(y) for y in open('day11-3in.txt').read().split('\n')][::-1]
# not a general solution, relies on input numbers being in order, which is probably true for all inputs
average = (int) (sum(f)/len(f))
tly = 0
for i in f:
  if i < average:
    tly += average - i
print(tly)
