t = int(input())
for _ in range(t):
    a, b, n, s = (int(i) for i in input().split())
    res = "YES" if s - n * min(a, s // n) <= b else "NO"
    print(res)
