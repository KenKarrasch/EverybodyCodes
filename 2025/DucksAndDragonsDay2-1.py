f = open('day2-1in.txt').read()
print(f)
x = int(f.split('[')[1].split(',')[0])
y = int(f.split(',')[1].split(']')[0])


A = [x,y]
R = [0,0]
print(x,y)

def add(X1,Y1,X2,Y2):
    return([X1 + X2, Y1 + Y2])

def mult(X1,Y1,X2,Y2):
    return([X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2])

def div(X1,Y1,X2,Y2):
    return([int(X1 / X2),int(Y1 / Y2)])

for i in [0,1,2]:
    R = mult(R[0],R[1],R[0],R[1])
    print(R)
    R = div(R[0],R[1],10,10)
    print(R)
    R = add(R[0],R[1],A[0],A[1])
    print(R)

print(R)
