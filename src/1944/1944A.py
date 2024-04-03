t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = n if k < n - 1 else 1
    print(res)
