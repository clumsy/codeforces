n, m = (int(i) for i in input().split())
res = True
for _ in range(n):
    s = input()
    res &= all(c in ["B", "G", "W", " "] for c in s)
res = "#Black&White" if res else "#Color"
print(res)
