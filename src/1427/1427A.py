t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    s = sum(a)
    if s == 0:
        print("NO")
    else:
        print("YES")
        gt0 = [i for i in a if i > 0]
        lt0 = [i for i in a if i < 0]
        res = (gt0 + lt0) if s > 0 else (lt0 + gt0)
        res += [0] * (n - len(gt0) - len(lt0))
        print(*res)
