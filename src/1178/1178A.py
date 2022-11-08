n, a = int(input()), [int(i) for i in input().split()]
c = [1] + [i + 1 for i in range(1, n) if a[i] <= a[0] // 2]
res = c if 2 * sum(a[i - 1] for i in c) > sum(a) else [0]
if res != [0]:
    print(len(res))
print(*res)
