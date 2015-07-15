a = int(raw_input())
d=a
b=[]
count = rev_count=0
for i in xrange(0,a):
    d-=1
    c = list(map(int,raw_input().strip().split(" ")))
    count += c[i]
    rev_count+=c[d]
print abs(count-rev_count)
    