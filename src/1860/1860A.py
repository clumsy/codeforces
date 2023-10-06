t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    res = "(" * n + ")" * n
    if s in res:
        res = "()" * n
        res = res if s not in res else None
    print("YES" if res else "NO")
    if res:
        print(res)
