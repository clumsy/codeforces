t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = max(int(i) for i in input().split())
    res = []
    for _ in range(m):
        s = input()
        o, l, r = s[0], *(int(i) for i in s[1:].split())
        if l <= a <= r:
            a += 1 if o == "+" else -1
        res.append(a)
    print(*res)
