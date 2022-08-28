t = int(input())
for _ in range(t):
    m, s = input(), input()
    m = {c: i for i, c in enumerate(m)}
    res = sum(abs(m[s[i]] - m[s[i - 1]]) for i in range(1, len(s)))
    print(res)
