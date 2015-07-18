t = input()
for i in range(0,t):
    s = raw_input()
    count=0
    for i in range(0,len(s)/2):
        count+=abs(ord(s[i])-ord(s[-i-1]))
    print count