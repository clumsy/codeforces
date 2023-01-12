n, q = (int(i) for i in input().split())
s = [c for c in input()]
for i, e in enumerate(s):
    s[i] = ord(e) - ord("a") + 1 + (s[i - 1] if i > 0 else 0)
for _ in range(q):
    l, r = (int(i) for i in input().split())
    res = s[r - 1] - (s[l - 2] if l > 1 else 0)
    print(res)
