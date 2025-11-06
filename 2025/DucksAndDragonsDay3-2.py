f = open('day3-2in.txt').read()
s = [int(i) for i in f.split(',')]
s.sort(reverse=True)
st = [s[0]]
for i in range(1,len(s)):
    if s[i] < st[-1]:
        st.append(s[i])
print(sum(st[-20:]))
