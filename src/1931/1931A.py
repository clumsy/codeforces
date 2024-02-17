t = int(input())
for _ in range(t):
    n = int(input())
    s, i = [], 2
    while n:
        c = min(26, n - i)
        n -= c
        s.append(chr(ord("a") + c - 1))
        i -= 1
    res = "".join(s[::-1])
    print(res)
