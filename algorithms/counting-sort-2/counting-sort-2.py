from collections import Counter
t = input()
nums = Counter(map(int, raw_input().split()))
for i in xrange(0,100):
	if i in nums:
		for j in range(nums[i]):
			print i,