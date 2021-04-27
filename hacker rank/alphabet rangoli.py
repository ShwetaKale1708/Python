#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

n=int(input())
for i in range(1,n+1):

    print("-"*((n-i)*2),end='')
    for j in range(i):
        if i==1:
            print(chr((96+n)-j),end='')

        else:print(chr((96+n)-j),end='-')
    for k in range(1,i):
        if k==i-1:
            print(chr(97 + n - i + k), end='')
            break
        print(chr(97+n-i+k),end='-')
    for ss in range(0,((n*2)-(i*2))):
        print("-",end="")
    print()
for i in range(n-1,0,-1):
    print("-"*((n-i)*2),end='')

    for j in range(i):
        print(chr((96+n)-j),end='-')
    for k in range(i-1,0,-1):
        print(chr((97+n)-k),end='-')
    for ss in range(1,((n*2)-(i*2))):
        print("-",end="")
    print()