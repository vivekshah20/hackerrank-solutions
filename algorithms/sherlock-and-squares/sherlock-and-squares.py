import math
t = int(raw_input())
for i in range(0,t):
    num1, num2 = map(int,raw_input().strip().split(" "))
    count = math.floor(math.sqrt(num2))-math.floor(math.sqrt(num1-1))
    count = str(count).split(".")
    print count[0]