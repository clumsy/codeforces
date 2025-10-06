t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, mex = 0, set(range(k))
    for i in a:
        if i in mex:
            mex.remove(i)
        res += i == k
    res = max(res, len(mex))
    print(res)
