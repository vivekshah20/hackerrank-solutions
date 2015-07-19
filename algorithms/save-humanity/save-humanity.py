"""
Working on the solution
"""
t = input()
for i in xrange(t):
	string, substring = raw_input().split()
	string, substring = list(string),list(substring)
	l_string = len(string)
	l_substring = len(substring)
	ord_string = [ord(i) for i in string]
	ord_substring = [ord(i) for i in substring]
	print ord_string, ord_substring
	# for j in 
