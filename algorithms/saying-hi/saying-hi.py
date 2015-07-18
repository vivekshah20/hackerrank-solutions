import re
regex = re.compile(r"hi\s[^d]",re.IGNORECASE)
t = input()
for i in xrange(t):
    s = raw_input().strip()
    if regex.match(s):
        print s