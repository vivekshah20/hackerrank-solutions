import collections
t = input()

for i in range(0,t):
    
    string = raw_input().strip()
    substrings = (''.join(sorted(string[y : y + x])) for x in range(1, len(string)) for y in range(len(string) - x + 1))
    substrings = collections.Counter(substrings)

        # Count pairs for each set of anagrams
    print(sum(m * (m - 1) // 2 for m in substrings.values()))