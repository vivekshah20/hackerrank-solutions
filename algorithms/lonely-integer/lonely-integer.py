def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)