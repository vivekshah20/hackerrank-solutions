import re
testcases=input()
for i in xrange(testcases):
    s=raw_input()
    l = re.split(r"[-\s]",s)
    print "CountryCode="+l[0]+",LocalAreaCode="+l[1]+",Number="+l[2]