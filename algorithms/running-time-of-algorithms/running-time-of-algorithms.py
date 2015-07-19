s = input()
num = list(map(int,raw_input().split()))
count=0
for i in range(1,len(num)):
    for j in reversed(range(i)):
        if num[j+1]<num[j]:
            num[j], num[j + 1] = num[j + 1], num[j]
            count+=1
        else:
            break
print count