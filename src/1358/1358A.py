t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = (m * n + 1) // 2
    print(res)