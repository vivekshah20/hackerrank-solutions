# Enter your code here. Read input from STDIN. Print output to STDOUT
def two_arrays(a,b):
    for j in xrange(n):
        if a[j]+b[j]<k:
            return "NO"
    return "YES"
t = input()
for i in xrange(t):
    n,k= map(int,raw_input().split(" "))
    a=list(map(int,raw_input().split()))
    b=list(map(int,raw_input().split()))
    a=sorted(a)
    b=sorted(b,reverse=True)
    print two_arrays(a,b)