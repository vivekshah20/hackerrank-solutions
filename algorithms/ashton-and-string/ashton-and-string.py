"""
"set" data structure in python has a large RAM footprint and returns a MemoryError in case of very long string. Due to this, the solution can only pass
through the first 4 testcases. Any other solutions are welcome. :)
"""
n= input()
for i in range(n):
    s = raw_input()
    m=input()-1
    a = set()
    j = 1
    while True:
        for i in xrange(len(s)-j+1):   
            a.add(s[i:i+j])
        if j==len(s):
            break
        j+=1
    a=''.join(sorted(list(a)))
    print a[m]