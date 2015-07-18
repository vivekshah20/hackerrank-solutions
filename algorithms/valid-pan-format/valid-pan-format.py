import re
testcases=input()
pan_exp=re.compile(r"[A-Z]{5}\d{4}[A-Z]$")
for i in xrange(0,testcases):
    print "YES" if pan_exp.match(raw_input()) else "NO"