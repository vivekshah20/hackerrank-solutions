"""
O(N) Algorithm
"""
t = input()
for i in xrange(t):
	s = raw_input()
	first = 0
	last = len(s)-1
	while (first<last) and s[first]==s[last]:
		first+=1
		last-=1
	first_s= s[:first]+s[first+1:]
	last_s = s[:last]+s[last+1:]
	if first_s == first_s[::-1]:
		print first
	elif last_s == last_s[::-1]:
		print last
	else:
		print -1