t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = sorted([a + b, c + d])[1]
    print(res)
