from __future__ import division
t = input()
for i in xrange(0,t):
    a=b=0
    n = input()
    if n<3:
        print "-1"
    else:
        for i in range(n,-1,-1):
            
            if (i/3).is_integer() and ((n-i)/5).is_integer():
                a = i
                b = n-i
                break
        if a==0 and b==0:
            print "-1"
        else:
            print "5"*a+"3"*b