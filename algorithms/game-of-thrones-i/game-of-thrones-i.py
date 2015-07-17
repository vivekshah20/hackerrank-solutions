import collections
string = raw_input()
c = collections.Counter(string)
count=0
for k in c:
    count+=(c[k]%2)
if count > 1:
    print "NO"
else:
    print "YES"