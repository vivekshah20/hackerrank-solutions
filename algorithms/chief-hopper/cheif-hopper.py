N = input()
H = map(int, raw_input().split())
e=0
for i in reversed(range(N)):
    e = (e + H[i] + 1) // 2
print e