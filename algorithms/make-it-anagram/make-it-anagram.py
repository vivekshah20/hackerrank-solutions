# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
string1 = Counter(raw_input())
string2 = Counter(raw_input())
print sum((string1 - string2).values()) + sum((string2 - string1).values())