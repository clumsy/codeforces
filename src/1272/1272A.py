q = int(input())
for _ in range(q):
    a = sorted(int(i) for i in input().split())
    if a[2] - a[0] < 3:
        res = 0
    else:
        if a[0] == a[1]:
            a[0] += 1
            a[1] += 1
            a[2] -= 1
        else:
            a[2] -= 1
            a[1] -= 1
            a[0] += 1
        res = (a[1] - a[0]) + (a[2] - a[0]) + (a[2] - a[1])
    print(res)
