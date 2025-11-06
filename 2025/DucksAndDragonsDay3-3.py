f = open('day3-3in.txt').read()
s = [int(i) for i in f.split(',')]
s.sort(reverse=True)
bst = 1
for i in range(1,len(s)-1):        
    j = i + 1
    rn = 1
    dn = False
    while not dn and s[i] == s[j]:
        rn += 1
        j += 1
        if j >= len(s):
            dn = True
    bst = max(rn,bst)
print(bst)
