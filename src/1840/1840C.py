t = int(input())


def count(cur, k):
    # cur + 1 - k, cur + 1 - k - 1, ..., 1
    # (1 + (cur + 1 - k)) * (cur + 1 - k) / 2
    v = cur + 1 - k
    return ((1 + v) * v) // 2 if v > 0 else 0


for _ in range(t):
    n, k, q = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = cur = 0
    for i in a:
        if i > q:
            res += count(cur, k)
            cur = 0
        else:
            cur += 1
    res += count(cur, k)
    print(res)
