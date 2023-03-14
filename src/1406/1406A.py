from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), Counter(int(i) for i in input().split())
    mex1, mex2 = None, None
    for i in range(101):
        cnt = a.get(i, 0)
        if cnt == 0:
            mex1 = i
            mex2 = mex2 if mex2 is not None else i
            break
        elif cnt == 1:
            mex2 = mex2 if mex2 is not None else i
    res = mex1 + mex2
    print(res)
