t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = (n - 2 + x - 1) // x + 1 if n > 1 else 1
    print(res)
