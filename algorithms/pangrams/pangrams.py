string = raw_input()
if (len(set(string.lower()))) == 27:
    print "pangram"
else:
    print "not pangram"