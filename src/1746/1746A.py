t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = input().split()
    res = "YES" if a.count("0") != n else "NO"
    print(res)
