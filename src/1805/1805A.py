t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    x = 0
    for i in a:
        x ^= i
    res = 0 if x == 0 else x if n & 1 == 1 else -1
    print(res)
