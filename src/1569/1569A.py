t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = (
        (i + 1, i + 2) if (i := max(s.find(p) for p in ["ab", "ba"])) >= 0 else (-1, -1)
    )
    print(*res)
