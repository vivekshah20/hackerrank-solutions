input()
w= sorted(map(int,raw_input().split()))
max=w[0]+4
count=1
for a in w:
    if a>max:
        count+=1
        max=a+4
print count