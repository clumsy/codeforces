from collections import Counter

timur = Counter("Timur")
t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = n == 5 and Counter(s) == timur
    print("YES" if res else "NO")
