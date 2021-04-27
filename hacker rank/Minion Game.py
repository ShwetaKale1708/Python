#Question---> https://www.hackerrank.com/challenges/the-minion-game/problem

#Solution:
s=input()
length=len(s)
vow=0
con=0
for i in range(length):
    if s[i] in 'AEIOU':
        vow=vow+(length-i)
    else:
        con=con+(length-i)
if con>vow:
    print('Stuart',con)
elif vow>con:
    print('Kevin',vow)
else:
    print('Draw')