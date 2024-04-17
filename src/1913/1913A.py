t = int(input())
for _ in range(t):
    s = input()
    res = [-1]
    for i in range(1, len(s)):
        if s[i] != "0":
            a, b = int(s[:i]), int(s[i:])
            if b > a:
                res = [a, b]
            break
    print(*res)
