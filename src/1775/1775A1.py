t = int(input())
for _ in range(t):
    s = input()
    if s[:2] in ["aa", "ba"]:
        res = s[0], s[1], s[2:]
    else:
        res = s[0], s[1:-1], s[-1]
    print(*res)
