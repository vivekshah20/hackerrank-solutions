N,K=map(int,raw_input().split())
l =map(int,raw_input().split())
for i in xrange(len(l)):
    if K<=0:
        break
    maxi,idx=-1,0
    for j in xrange(i,len(l)):
        if l[j]>maxi:
            maxi=l[j]
            idx=j
    if idx!=i:
        K -= 1
        l[idx], l[i] = l[i], l[idx]
print " ".join(map(str,l))