t = int(input())
for _ in range(t):
    p, a, b, c = (int(i) for i in input().split())
    res = min((a - p) % a, (b - p) % b, (c - p) % c)
    print(res)
