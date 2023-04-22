from itertools import permutations

a = (int(i) for i in input().split())
res = "IMPOSSIBLE"
for a, b, c in permutations(a, 3):
    v = [a + b - c, b + c - a, a + c - b]
    if all(i > 0 for i in v):
        res = "TRIANGLE"
        break
    elif all(i >= 0 for i in v):
        res = "SEGMENT"
print(res)
