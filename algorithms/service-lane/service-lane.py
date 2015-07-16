n = list(map(int,raw_input().strip().split(" ")))
width = list(map(int,raw_input().strip().split(" ")))

for i in range(0,n[1]):
    t = list(map(int,raw_input().strip().split(" ")))
    a = min (s for s in width[t[0]:t[1]+1])
    print a