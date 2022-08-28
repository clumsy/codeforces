t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = "YES" if all(x % a[0] == 0 for x in a[1:]) else "NO"
    print(res)
