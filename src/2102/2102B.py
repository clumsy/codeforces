t = int(input())
for i in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    f = next(a)
    g = sum(abs(i) >= abs(f) for i in a)
    res = "YES" if g >= (n + 1) // 2 - 1 else "NO"
    print(res)
