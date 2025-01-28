def count(a):
    return sum((a[i] + a[i + 1]) == a[i + 2] for i in range(len(a) - 2))


t = int(input())
for _ in range(t):
    a = [int(i) for i in input().split()]
    res = max(
        count(a[:2] + [a[0] + a[1]] + a[2:]), count(a[:2] + [a[2] - a[1]] + a[2:])
    )
    print(res)
