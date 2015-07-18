import re
testcases=input()
t = re.compile(r"[a-z]{0,3}\d{2,8}[A-Z]{3}")
for i in xrange(testcases):
    print "VALID" if t.match(raw_input()) else "INVALID"