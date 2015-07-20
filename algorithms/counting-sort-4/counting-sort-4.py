n = input()
count = [0] * 100
num = [[] for i in xrange(100)]

for i in xrange(n):
    arr = raw_input().split()
    x = int(arr[0])
    count[x] = count[x] + 1
    num[x].append((i, arr[1]))
    
for i in xrange(100):
    for j in xrange(count[i]):
        if num[i][j][0] < n / 2:
            print "-",
        else:
            print num[i][j][1],