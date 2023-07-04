t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = (
        "YES"
        if all(abs(ord(s[i]) - ord(s[n - 1 - i])) in {0, 2} for i in range(n // 2))
        else "NO"
    )
    print(res)
