t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    res = 1 if b < a else (n + a - 1) // a
    print(res)
