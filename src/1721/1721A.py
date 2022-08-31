from collections import Counter

t = int(input())
for _ in range(t):
    image = input() + input()
    c = Counter(image)
    res = len(c.keys()) - 1
    print(res)
