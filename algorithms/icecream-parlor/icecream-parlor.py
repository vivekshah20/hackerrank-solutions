t = input()
for i in range(0,t):
    m = input()
    n = input()
    prices = list(map(int,raw_input().strip().split()))
    
    for i in range(0,n):
        for j in range(i+1,n):
            if ((prices[i]+prices[j])==m):
                print i+1,j+1
                break