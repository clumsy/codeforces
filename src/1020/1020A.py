n, h, a, b, k = (int(i) for i in input().split())
for _ in range(k):
    ta, fa, tb, fb = (int(i) for i in input().split())
    f = min(b, max(a, fa))
    res = abs(fa - fb) if ta == tb else abs(ta - tb) + abs(fa - f) + abs(fb - f)
    print(res)
