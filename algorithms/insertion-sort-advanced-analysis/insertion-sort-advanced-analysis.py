def sorting(a):
    l = len(a)
    if l==1:
        return 0
    m = l/2
    n = l - m
    a1 = a[:m]
    a2 = a[m:]
    ans = sorting(a1) + sorting(a2)
    count1 = 0
    count2 = 0
    for i in range(l):
        if count1 <m and (count2>=n or a1[count1]<=a2[count2]):
            a[i] = a1[count1]
            ans += count2
            count1 += 1 
        elif count2 < n:
            a[i] = a2[count2]
            count2 += 1
    return ans
n = input()
for iterate in range( n ):
    x = input()
    a = map(int,raw_input().strip().split())
    answer = sorting(a)
    print answer