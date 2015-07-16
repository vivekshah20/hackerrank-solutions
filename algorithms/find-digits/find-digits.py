a = int(raw_input())

for i in range(0,a):
    b = int(raw_input())
    m=b
    count =0
    while(b>0):
        c=b%10
        b=b/10
        if c ==0:
            continue
        if m%c ==0:
            count+=1
    print count