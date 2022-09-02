from collections import Counter

t = int(input())
for i in range(t):
    s = input()
    c = Counter(s)
    res = c["A"] + c["C"] == c["B"]
    print("YES" if res else "NO")
