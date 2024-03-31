t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    b = sorted(int(i) for i in input().split())
    c = sorted(int(i) for i in input().split())
    res, j = 0, m - 1
    for i in range(n):
        while j >= 0 and b[i] + c[j] > k:
            j -= 1
        res += j + 1
    print(res)
