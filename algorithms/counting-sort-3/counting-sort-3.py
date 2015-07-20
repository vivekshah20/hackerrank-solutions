from collections import Counter
t = input()
num=[]
for i in xrange(t):
    n,string = raw_input().split()
    num.append(n)
"""
If you try to convert the number (string to int) during 'append' itself then it will split the number and then store it
For e.g. 12 will be stored as a list [1,2] rather than [12]
"""
num = map(int,num) 
num = Counter(num)
count=0
for i in xrange(100):
    if i in num:
        count+=num[i]
        print count,
    else:   print count,