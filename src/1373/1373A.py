t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = -1 if a >= c else 1, -1 if c // b >= a else b
    print(*res)
