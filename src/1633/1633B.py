from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    c = Counter(s)
    # if clear minority - remove it, otherwise remove last and divide by 2
    res = min(c["0"], c["1"], (len(s) - 1) // 2)
    print(res)
