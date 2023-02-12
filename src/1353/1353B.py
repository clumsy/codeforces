t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    b = sorted((int(i) for i in input().split()), reverse=True)
    i = 0
    while i < k:
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
        i += 1
    res = sum(a)
    print(res)
