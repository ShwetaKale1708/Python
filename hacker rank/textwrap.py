#https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
s=input()
n=int(input())
c=0
a=n
b=a
aa=""
list=[]
for i in range(int((len(s)/n)+1)):
    aa=s[c:b]
    list.append(aa)
    c=b
    b=b+a
for j in list:
    print(j) 