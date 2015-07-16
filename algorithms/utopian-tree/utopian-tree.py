a=int(raw_input())
for i in xrange(0,a):
    b = int(raw_input())
    n=1
    if b==0:
        print n
        continue
    for j in xrange(1,b+1):
        
        if j%2==0:
            n+=1
        else:
            n*=2
    print n