t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    max_a, max_b = 1, 1
    for i in range(n):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        max_a, max_b = max(max_a, a[i]), max(max_b, b[i])
    print(max_a * max_b)
