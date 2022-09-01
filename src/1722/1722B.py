t = int(input())
for _ in range(t):
    n, r1, r2 = int(input()), input(), input()
    res = not any((c1, c2).count("R") == 1 for c1, c2 in zip(r1, r2))
    print("YES" if res else "NO")
