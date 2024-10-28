t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    # a - x = b - 2x => x = b - a
    res = max(0, a - max(0, b - a))
    print(res)
