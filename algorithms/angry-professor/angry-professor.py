# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for i in range(0,n):
    count =0
    num = list(map(int,raw_input().strip().split(" ")))
    t = list(map(int,raw_input().strip().split(" ")))
    for k in t:
        if k<=0:
            count+=1
    if count >= num[1]:
        print "NO"
    else: print "YES"