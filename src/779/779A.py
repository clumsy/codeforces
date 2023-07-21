from collections import Counter

n = int(input())
a = Counter(int(i) for i in input().split())
b = Counter(int(i) for i in input().split())
c = a + b
res = (
    -1
    if any(v & 1 == 1 for v in c.values())
    else sum(abs(v // 2 - a[k]) for k, v in c.items()) // 2
)
print(res)
