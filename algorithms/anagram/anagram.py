# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
t = input()
for i in range(0, t):
    s = raw_input()
    if (len(s) % 2 == 0):
        s1 = Counter(s[:len(s) / 2])
        s2 = Counter(s[len(s) / 2:len(s)])
        print sum((s2 - s1).values())
    else:
        print "-1"