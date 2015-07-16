from sys import exit
a = raw_input()

if "PM" in a:
    b=int(a[:2])
    if b == 12:
        print a[:8]
        exit(0)
    b=b+12
    a=str(b)+a[2:8]
    print a
if "AM" in a:
    b=int(a[:2])
    if b == 12:
        print "00"+a[2:8]
        exit(0)
    print a[:8]