import re
n = input()
s=""
for i in xrange(n):
    s+=raw_input()+" "
t=input()
for i in xrange(t):
    sub = raw_input()
    regex=re.compile(r"\w(%s)\w"%sub)
    print len(regex.findall(s))