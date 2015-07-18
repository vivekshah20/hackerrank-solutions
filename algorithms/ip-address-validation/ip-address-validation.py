import re
t = input()
byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'  # 0 - 255
ipv4_regex = '^{0}(\.{0}){{3}}$'.format(byte)
ipv4_regex = re.compile(ipv4_regex)
hex_group = '[0-9A-Fa-f]{1,4}'  # Four hex digits
ipv6_regex = '^({0})(:{0}){{7}}$'.format(hex_group)
ipv6_regex =re.compile(ipv6_regex)
for i in xrange(t):
    ip = raw_input()
    if ipv4_regex.match(ip):
        print "IPv4"
    elif ipv6_regex.match(ip):
        print "IPv6"
    else:
        print "Neither"