t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    # if any dupe -> YES, otherwise no sums will match
    res = "YES" if len(set(a)) != n else "NO"
    print(res)
