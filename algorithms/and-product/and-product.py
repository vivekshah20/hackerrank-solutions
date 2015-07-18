__author__ = 'Vivek Shah'

t = input()
for i in range(0,t):
    A,B = map(int,raw_input().split())
    x = 0
    while (A | x) < B:
        x = (x << 1) | 1
        
    print(A & ~x)