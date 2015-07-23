t = input()
for i in xrange(t):
    n  = input()
    ch = []
    for i in xrange(n):
        ch1=list(raw_input())
        ch1.sort()
        ch.append(ch1)
    flag=True
    for i in xrange(n):
        for j in xrange(n-1):
            if ch[j][i]>ch[j+1][i]:
                flag = False
    if flag:
        print "YES"
    else:
        print "NO"