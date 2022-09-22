q = int(input())
for _ in range(q):
    a, b, c = sorted([int(i) for i in input().split()])
    res = a + min(b - a, c) + (c - min(b - a, c)) // 2  # (a + b + c) // 2
    print(res)
