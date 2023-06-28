n = int(input())
for _ in range(n):
    k, x = (int(i) for i in input().split())
    res = x + (k - 1) * 10 - (k - 1)
    print(res)
