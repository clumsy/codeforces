t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = g = 0
    for i in a:
        if i >= k:
            g += i
        elif i == 0:
            if g > 0:
                res += 1
                g -= 1
    print(res)
