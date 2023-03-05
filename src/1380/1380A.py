t = int(input())
for _ in range(t):
    n, p = int(input()), [int(i) for i in input().split()]
    lft, rgt = [0] * n, [n - 1] * n
    for i in range(1, n - 1):
        lft[i] = i if p[i] < p[lft[i - 1]] else lft[i - 1]
        k = n - 1 - i
        rgt[k] = k if p[k] < p[rgt[k + 1]] else rgt[k + 1]
    res = None
    for j in range(1, n - 1):
        if p[lft[j - 1]] < p[j] > p[rgt[j + 1]]:
            res = lft[j - 1] + 1, j + 1, rgt[j + 1] + 1
            break
    if res:
        print("YES")
        print(*res)
    else:
        print("NO")
