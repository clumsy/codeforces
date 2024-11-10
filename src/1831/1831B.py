t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())

    def count(x):
        cnt, prv, cur = {}, 0, 0
        for i in x:
            if i == prv:
                cur += 1
            else:
                prv, cur = i, 1
            cnt[i] = max(cnt.get(i, 0), cur)
        return cnt

    cnt_a, cnt_b = count(a), count(b)
    res = 0
    for i in cnt_a:
        res = max(res, cnt_a[i] + cnt_b.get(i, 0))
    for i in cnt_b:
        res = max(res, cnt_b[i] + cnt_a.get(i, 0))
    print(res)
