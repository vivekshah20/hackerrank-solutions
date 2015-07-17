n = int(raw_input())
for i in range(0,n):
    s = raw_input()
    rs = s[::-1]
    s=list(s)
    rs=list(rs)
    count=0
    for k in xrange(0,len(s)-1):
        if abs(ord(s[k])-ord(s[k+1])) == abs(ord(rs[k])-ord(rs[k+1])):
            continue
        else:
            print "Not Funny"
            count=1
            break
    if count !=1:
        print "Funny"