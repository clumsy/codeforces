t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    diff = a - (2 * c - b if c > b else b)
    res = 2 if diff > 0 else 1 if diff < 0 else 3
    print(res)
