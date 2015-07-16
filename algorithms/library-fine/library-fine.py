a = list(map(int,raw_input().strip().split(" ")))
b= list(map(int,raw_input().strip().split(" ")))


if a[2]>b[2]:
    print 10000
elif a[2]<b[2]:
    print 0
elif a[1]>b[1]:
    print (a[1]-b[1])*500
elif a[1]<b[1]:
    print 0
elif a[0]>b[0]:
    print (a[0]-b[0])*15
else:
    print 0