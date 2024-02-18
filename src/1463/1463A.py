t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    # e + a1, e + b1, e + c1 = a, b, c
    # 3e + 6e = a + b + c
    d, r = divmod(a + b + c, 9)
    res = "YES" if r == 0 and min(a, b, c) >= d else "NO"
    print(res)
