from collections import Counter

n, a = int(input()), Counter(int(i) for i in input().split())
dupes = {k: v for k, v in a.items() if v > 1}
if any(v > 2 for v in dupes.values()):
    print("NO")
else:
    print("YES")
    print(len(a))
    print(*sorted(a))
    print(len(dupes))
    print(*sorted(dupes.keys(), reverse=True))
