t = int(input())
for _ in range(t):
    s = [int(i) for i in input().split()]
    res = "YES" if max(s[:2]) + max(s[2:]) == sum(sorted(s)[2:]) else "NO"
    print(res)
