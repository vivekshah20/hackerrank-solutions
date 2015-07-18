import re
regex = re.compile('^[_\.]\d+[a-z]*_?$', re.IGNORECASE)
t=input()
for i in xrange(t):
    print "VALID" if regex.match(raw_input()) else "INVALID"