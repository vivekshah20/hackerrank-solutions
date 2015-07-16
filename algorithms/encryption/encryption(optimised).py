import math
s = raw_input()
l = len(s)
cols = int(math.ceil(math.sqrt(l)))
for i in xrange(0,cols):
    print s[i::cols],