import re
n = input()
sentences=[]
for i in xrange(n):
    sentences.extend(list(raw_input().split()))
t = input()
for i in xrange(t):
    word = raw_input()
    bword = re.sub("our","or",word)
    count=0
    for each in sentences:
        if word==each or bword ==each:
            count+=1
    print count