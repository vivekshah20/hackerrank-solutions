def can_reverse(a):
    i = l
    while i < r:
        if a[i] < a[i + 1]:
            return False
        i += 1
    return True

def can_swap(a):
    i = l + 1
    while i + 1 < r:
        if a[i] > a[i + 1]:
            return False
        i += 1
    if a[l] < a[r - 1]:
        return False
    if a[r] > a[l + 1]:
        return False
    return True


n = input()
a = map(int, raw_input().split())
s = sorted(a)
l = 0
while (l < n) and (a[l] == s[l]):
    l += 1
r = n - 1
while (r >= 0) and (a[r] == s[r]):
    r -= 1
if l >= r:
    print "yes"
else:
    swap = can_swap(a)
    rev = can_reverse(a)
    if not swap and not rev:
        print "no"
    else:
        print "yes"
        if swap:
            print "swap", l + 1, r + 1
        else:
            print "reverse", l + 1, r + 1