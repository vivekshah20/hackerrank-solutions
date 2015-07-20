from collections import Counter
t = input()
for i in range(t):
    n = input()
    num = sorted(map(int, raw_input().split()))
    num=Counter(num)
    count=0
    for j in num.values():
        count+= j*(j-1)
    print count