a = int(raw_input())

for i in range(0,a):
    b = raw_input()
    if (b[:10]=="hackerrank" and b[-10:]=="hackerrank"):
        print 0
    elif b[:10] =="hackerrank":
        print 1
    elif b[-10:]=="hackerrank":
        print 2
    else:
        print -1