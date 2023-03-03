t = int(input())
for _ in range(t):
    n, s = int(input()), [int(i) for i in input()]
    while s and s[-1] & 1 == 0:
        s.pop()
    if sum(s) & 1 != 0:
        for i in range(len(s) - 1):
            if s[i] & 1 == 1 and (i > 0 or s[i + 1] != 0):
                s = s[:i] + s[i + 1 :]
                break
    res = -1 if not s or sum(s) & 1 == 1 else "".join(str(i) for i in s)
    print(res)
