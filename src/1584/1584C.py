t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    res = "YES"
    for a, b in zip(a, b):
        if not (0 <= b - a <= 1):
            res = "NO"
            break
    print(res)
