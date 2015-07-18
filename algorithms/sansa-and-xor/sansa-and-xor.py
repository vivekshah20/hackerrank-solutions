__author__ = 'Vivek Shah'

t=input()
for i in range(0,t):
    n = input()
    num = map(int,raw_input().split(' '))
    result=0
    for i, value in enumerate(num):
        if (i+1)*(n-i)%2==1:
            result ^=value
    print result