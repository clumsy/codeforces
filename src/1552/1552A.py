t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = sum(f != s for f, s in zip(s, sorted(s)))
    print(res)
