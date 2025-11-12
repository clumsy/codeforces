t = int(input())
for _ in range(t):
    r0, x, d, n = (int(i) for i in input().split())
    s = input()
    res = 0
    for c in s:
        if c == "1" or r0 < x:
            res += 1
            r0 = max(0, r0 - d)
    print(res)
