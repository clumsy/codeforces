t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    res = cat = 0
    for i in reversed(range(k)):
        if cat >= a[i]:
            break
        res += 1
        cat += n - a[i]
    print(res)
