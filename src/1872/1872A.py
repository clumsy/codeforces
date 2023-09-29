t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    a, b = sorted([a, b])
    res = (b - (a + b) // 2 + c - 1) // c
    print(res)
