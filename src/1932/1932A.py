t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    end = s.find("**")
    s = s[: end if end >= 0 else n]
    res = s.count("@")
    print(res)
