"""
O(N^2) Solution
"""
t = input()
for i in xrange(t):
	string = raw_input()
	print string
	if string == string[::-1]:
		print "-1"
	else:
		for i in xrange(len(string)):
			s = string[0:i]+string[i+1:len(string)]
			if s == s[::-1]:
				print i