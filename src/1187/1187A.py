t = int(input())
for _ in range(t):
    n, s, t = (int(i) for i in input().split())
    # s0 + st = s
    # t0 + st = t
    # s0 + t0 + st = n
    # st = s + t - n
    # st = s + t - n
    st = s + t - n
    s0, t0 = s - st, t - st
    res = max(s0, t0) + 1
    print(res)
