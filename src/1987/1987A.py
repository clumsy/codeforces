t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = (n - 1) * k + 1
    print(res)
