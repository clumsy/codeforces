t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    p = next(a)
    res = "YES"
    for i in a:
        if abs(i - p) not in {5, 7}:
            res = "NO"
            break
        p = i
    print(res)
