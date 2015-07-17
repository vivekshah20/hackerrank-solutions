string = set("abcdefghijklmnopqrstuvwxyz")
t = input()
for i in range(0,t):
    s = set(raw_input().strip())
    string &= s
print len(string)