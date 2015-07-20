N, K, Q = list(map(int, raw_input().split()))
num = list(map(int, raw_input().split()))
for i in range(Q):
    idx = input()
    print(num[(idx - K) % N])