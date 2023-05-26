t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = e = False
    for _ in range(n):
        l_, r_ = (int(i) for i in input().split())
        s |= l_ == k
        e |= r_ == k
    res = "YES" if s and e else "NO"
    print(res)
