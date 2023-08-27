t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for _ in range(n):
        a, b = (int(i) for i in input().split())
        res += b < a
    print(res)
