t = int(input())
for _ in range(t):
    n, s = int(input()), list(input())
    e = next((i for i in range(n) if s[i] != "?"), n)
    if e == n:
        res = "".join("RB"[i & 1] for i in range(n))
    else:
        for i in range(e - 1, -1, -1):
            s[i] = "R" if s[i + 1] == "B" else "B"
        for i in range(e + 1, n):
            s[i] = s[i] if s[i] != "?" else "R" if s[i - 1] == "B" else "B"
        res = "".join(s)
    print(res)
