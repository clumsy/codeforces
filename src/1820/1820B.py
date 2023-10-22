t = int(input())
for _ in range(t):
    s = input()
    if all(c == "1" for c in s):
        res = len(s) ** 2
    else:
        n = max(len(c) for c in (s + s).split("0"))
        res, i = n, 1
        while n - i + 1 >= i:
            res = max(res, (n - i + 1) * i)
            i += 1
    print(res)
