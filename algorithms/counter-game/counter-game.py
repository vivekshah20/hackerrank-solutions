t = input()
for i in range(0,t):
    num = input()
    if num ==1:
        print "Richard"
    else:
        count =0
        while(num>1):
            
            temp = num
            while temp % 2 ==0:
                temp //=2
            if temp == 1:
                num //=2
                count+=1
            else:
                largest_pow = 1
                while ((largest_pow*2)<num):
                    largest_pow*=2
                num-=largest_pow
                count+=1
        if count %2==0:
            print "Richard"
        else:
            print "Louise"