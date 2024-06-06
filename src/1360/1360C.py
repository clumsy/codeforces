t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    odd = evn = 0
    ner = False
    for i, e in enumerate(a):
        odd += e & 1
        evn += 1 - (e & 1)
        ner |= i > 0 and e - a[i - 1] == 1
    res = "YES" if odd & 1 == 0 or ner else "NO"
    print(res)
