t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES" if any(s[i : i + 2] in s[i + 2 :] for i in range(n - 2)) else "NO"
    print(res)
