from collections import Counter

t = int(input())
for _ in range(t):
    p, h = input(), input()
    eq = {c: c not in p for c in [chr(i + ord("a")) for i in range(26)]}
    cnt, cnt_p = Counter(), Counter(p)

    def update(c, v):
        diff = -eq[c]  # previously matched, now need to re-check
        cnt[c] += v
        eq[c] = cnt[c] == cnt_p[c]
        diff += eq[c]
        return diff

    matches, n, res = 0, len(p), "NO"
    for i, c in enumerate(h):
        matches += update(c, 1)
        if i >= n:
            matches += update(h[i - n], -1)
        if matches == len(cnt_p):
            res = "YES"
            break
    print(res)
