import string

t = int(input())
for _ in range(t):
    s = input()
    res = "".join(sorted(s)) == string.ascii_lowercase[: len(s)]
    if res:
        left, right = s.split("a")
        res = [*left] == sorted(left, reverse=True) and [*right] == sorted(right)
    res = "YES" if res else "NO"
    print(res)
