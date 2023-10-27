t = int(input())
for _ in range(t):
    a = int(input())
    # a*n=180*(n-2) => n*(180-a)=360
    _, r = divmod(360, 180 - a)
    res = "YES" if r == 0 else "NO"
    print(res)
