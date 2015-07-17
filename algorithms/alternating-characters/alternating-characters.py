t = input()
for i in range(0,t):
    s = list(raw_input())
    count =0
    for i in range(0,len(s)-1):
        if (s[i]==s[i+1]):
            count+=1
    print count