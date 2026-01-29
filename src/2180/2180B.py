t = int(input())
for _ in range(t):
    n, a = int(input()), input().split()
    res = ""
    for w in a:
        res = min(res + w, w + res)
    print(res)
