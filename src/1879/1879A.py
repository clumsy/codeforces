t = int(input())
for _ in range(t):
    n = int(input())
    s, e = [0] * n, [0] * n
    for i in range(n):
        s[i], e[i] = (int(i) for i in input().split())
        if i == 0:
            res = s[i]
        elif s[i] >= s[0] and e[i] >= e[0]:
            res = -1
    print(res)
