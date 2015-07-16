a = int(raw_input())
b = list(map(int, raw_input().strip().split(" ")))

while (len(b) != 0):
    mini = min(b)
    # print mini
    print len(b)
    b = filter(lambda x: x != mini, b)
    b[:] = [x - mini for x in b]