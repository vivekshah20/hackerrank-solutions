from sys import maxint
n = input()
num = map(int, raw_input().split())
num.sort()
pairs=[]
d = maxint
for i in range(len(num)-1):
    diff = num[i+1]-num[i]
    if diff < d:
        d=diff
        pairs=[(num[i],num[i+1])]
    elif d == diff:
        pairs.append((num[i],num[i+1]))
for each in pairs:
    print each[0], each[1],