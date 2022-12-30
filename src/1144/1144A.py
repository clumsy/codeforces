n = int(input())
for _ in range(n):
    s = sorted(input())
    res = "YES"
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) != 1:
            res = "NO"
            break
    print(res)
