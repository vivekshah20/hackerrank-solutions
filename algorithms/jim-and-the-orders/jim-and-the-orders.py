def solve(cipher):
    A = cipher
    n = len(A)
    idx = sorted(range(n), key=lambda k: A[k][0]+A[k][1])
    return " ".join(map(lambda x: str(x+1), idx))

n = input()
cipher = []
for i in xrange(n):
    t = map(int, raw_input().strip().split(' '))
    cipher.append(tuple(t))

    s = "%s\n"%(solve(cipher))
print s,