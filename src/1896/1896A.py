t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    fst = next(a)
    res = "YES" if fst == min(fst, min(a)) else "NO"
    print(res)
