from math import inf

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    mi, mi_cnt, ma, ma_cnt = inf, 0, -inf, 0
    for i in a:
        if i < mi:
            mi, mi_cnt = i, 0
        mi_cnt += i == mi
        if i > ma:
            ma, ma_cnt = i, 0
        ma_cnt += i == ma
    res = 2 * mi_cnt * ma_cnt if mi != ma else mi_cnt * (mi_cnt - 1)
    print(res)
