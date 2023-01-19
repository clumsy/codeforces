t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = ("abc" * ((n + 2) // 3))[:n]
    print(res)
