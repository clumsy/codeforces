t = int(input())
for _ in range(t):
    n = int(input())
    mw = mh = 0
    for _ in range(n):
        w, h = (int(i) for i in input().split())
        mw, mh = max(mw, w), max(mh, h)
    res = 2 * (mw + mh)
    print(res)
