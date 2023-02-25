t = int(input())
for _ in range(t):
    s = list(input())
    s[0] = s[-1]
    res = "".join(s)
    print(res)
