n = int(input())
s = (input() for _ in range(n))
had = set()
for i in s:
    res = "YES" if i in had else "NO"
    had.add(i)
    print(res)
