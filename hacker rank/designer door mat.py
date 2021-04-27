#https://www.hackerrank.com/challenges/designer-door-mat/problem

s=input().split()
n=list(map(int,s))
a=n[0]
b=n[1]
for j in range(1,(a-2)+1,2):
    print((".|."*j).center(b,'-'))
print("WELCOME".center(b,'-'))
for i in range((a-2),0,-2):
    print(('.|.'*i).center(b,'-'))