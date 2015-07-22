t=input()
for i in range(t):
    input()
    num = map(int,raw_input().split())
    left_index =0
    right_index=len(num)-1
    left_sum=num[left_index]
    right_sum=num[right_index]
    while left_index != right_index:
        if left_sum < right_sum:
            left_index+=1
            left_sum+=num[left_index]
        else:
            right_index -=1
            right_sum+=num[right_index]
    if left_sum==right_sum:
        print "YES"
    else:
        print "NO"