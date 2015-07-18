import re
t = input()
regex = re.compile(r"^\([-+]?((([1-9]|[1-8]\d)(\.\d+)?)|90(\.0+)?), [-+]?((([1-9]\d?|1[0-7]\d)(\.\d+)?)|180(\.0+)?)\)$")
for i in xrange(t):
    latlong=raw_input()
    print "Valid" if regex.match(latlong) else "Invalid"