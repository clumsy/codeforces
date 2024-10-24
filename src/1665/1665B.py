def ceil_log2(x):
    """Return the ceiling of log2(x) using bit manipulation."""
    if x <= 1:
        return 0
    # Count the number of bits required to represent x
    return x.bit_length() - 1 + (1 if (1 << (x.bit_length() - 1)) < x else 0)


t = int(input())
for _ in range(t):
    n, a = int(input()), (i for i in input().split())
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
    cnt = max(cnt.values())
    res = ceil_log2((n + cnt - 1) // cnt) + (n - cnt) if cnt != n else 0
    # cnt * 2^x = n
    # 2 5 7 6 3
    # 2 5 7 6 3 | 2 5 7 6 3
    # 2 2 7 6 3 | ...
    # 2 2 7 6 3 | 2 2 7 6 3
    # 2 2 2 6 3 | ...
    # 2 2 2 2 3 | ...
    # 2 2 2 2 3 | 2 2 2 2 3
    # 2 2 2 2 2 | ...
    print(res)
