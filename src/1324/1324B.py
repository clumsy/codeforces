from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    bth = set()
    rgt, res = Counter(a), "NO"
    for i in a:
        rgt[i] -= 1
        if rgt[i] == 0 and i in bth:
            bth.remove(i)
        if bth:
            res = "YES"
            break
        if rgt[i] > 0:
            bth.add(i)
    print(res)
