t = input()
count=0
for i in xrange(t):
    s = raw_input().lower()
    if "hackerrank" in s:
        count+=1
print count