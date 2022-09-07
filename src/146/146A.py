n = int(input())
s = [int(i) for i in input()]
res = s.count(7) + s.count(4) == n and sum(s[: n // 2]) == sum(s) // 2
print("YES" if res else "NO")
