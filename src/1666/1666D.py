from collections import Counter

t = int(input())
for _ in range(t):
    s, t = input().split()
    cnt_s, cnt_t = Counter(s), Counter(t)
    s = list(s)
    for i, c in enumerate(s):
        if cnt_s[c] > cnt_t[c]:
            s[i] = ""
            cnt_s[c] -= 1
    res = "YES" if "".join(s) == t else "NO"
    print(res)
