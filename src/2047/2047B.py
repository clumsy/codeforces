t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ma_c = mi_c = None
    cnt = {}
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
    for c in cnt:
        if not ma_c or (cnt[ma_c] < cnt[c] or (cnt[ma_c] == cnt[c] and ma_c > c)):
            ma_c = c
        if not mi_c or (cnt[mi_c] > cnt[c] or (cnt[mi_c] == cnt[c] and mi_c < c)):
            mi_c = c
    i = next((i for i, c in enumerate(s) if c == mi_c), 0)
    res = s[:i] + ma_c + s[i + 1 :]
    print(res)
