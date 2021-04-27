#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n=int(input())
A=set(int(x) for x in input().split(' '))
list=list(A)
points=sorted(list)
index=points.index(max(points))
print(points[index-1])