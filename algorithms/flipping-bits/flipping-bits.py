__author__ = "Vivek Shah"
t = input()
for i in range(0,t):
    n = input()
    print int(''.join('1' if x=='0' else '0' for x in bin(n)[2:].zfill(32)),2)