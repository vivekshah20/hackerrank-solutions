from collections import Counter
t= input()
A = Counter(map(int,raw_input().split()))
t=input()
B = Counter(map(int,raw_input().split()))
s=[]
for each in A:
    if A[each] != B[each]:
        print each,