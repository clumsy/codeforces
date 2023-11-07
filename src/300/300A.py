n, a = int(input()), sorted(int(i) for i in input().split())
res = ([a[0]], [a[-1]], [*a[1:-1]]) if a[-1] > 0 else ([a[0]], [*a[1:3]], [*a[3:]])
for i in res:
    print(len(i), *i)
