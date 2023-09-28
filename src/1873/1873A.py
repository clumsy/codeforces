t = int(input())
for _ in range(t):
    s = input()
    res = "YES" if sum(c1 == c2 for c1, c2 in zip(s, "abc")) > 0 else "NO"
    print(res)
