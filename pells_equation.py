#finding Integer solutions of the equation X^2 - N*Y^2 = 1
#True only if N is not a some square


import math

def find(X,Y,K):
    M=1
    i=abs(K)
    while True:
        b=(X+Y*M)/abs(K)
        if b == math.floor(b):
            if (abs(M**2 - n)) < i:
                i=abs(M**2 - n)

            else:
                break
        M+=1

    return M



#global n
print('This program gives the integer solution to the equation  X^2 - N*Y^2 = 1 for different Values of "N"\n')
n = int(input('What is the value of N'))

x=2
y=1

k= x**2 - n*(y**2)

while math.floor(k) != 1:
    m=find(x,y,k)
    a=(x*m + n*y)/abs(k)
    b=(x+y*m)/abs(k)
    k=(m**2 - n)/k
    x=a
    y=b

print('Value of X = ',x,'\nValue of Y = ',y)

