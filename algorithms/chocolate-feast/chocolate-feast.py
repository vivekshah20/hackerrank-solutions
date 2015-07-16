T = int(raw_input())
for i in range (0,T):
    n,c,m = [int(x) for x in raw_input().split(' ')]
    count=0
    no = n/c
    count+=no
    while (no>=m):
        count+=(no/m)
        no=(no/m)+(no%m)
    print count