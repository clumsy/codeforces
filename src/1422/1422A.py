t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = max(a, b, c)
    print(res)
