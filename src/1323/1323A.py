t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()][:2]
    if sum(a) & 1 == 0:
        res = [i + 1 for i in range(len(a))]
    else:
        res = [next((i + 1 for i, e in enumerate(a) if e & 1 == 0), -1)]
    if res != [-1]:
        print(len(res))
    print(*res)
