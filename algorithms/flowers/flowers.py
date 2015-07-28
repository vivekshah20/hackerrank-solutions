N, K = map(int,raw_input().split())
C = sorted(map(int,raw_input().split()),reverse=True)
count= N/K+1
cost=0
for i in xrange(count):
    cost += (i+1)*sum(C[i*K:(i+1)*K])
print cost