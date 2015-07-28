N, M = map(int, raw_input().strip().split())
queries,q = [],[]
for i in xrange(M):
    queries.append(map(int, raw_input().strip().split()))
for each in queries:
    q.append((each[0],each[2]))
    q.append((each[1]+1,-each[2]))
q.sort(key= lambda x: (x[0],x[1]))
maxi,c=-1<<32,0
for i in q:
    c+=i[1]
    maxi=max(maxi,c)
print maxi