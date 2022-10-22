t = int(input())
for _ in range(t):
    k, s = int(input()), input()
    res, last = 0, None
    for i in range(k):
        if s[i] == "A":
            last = i
        elif last is not None:
            res = max(res, i - last)
    print(res)
