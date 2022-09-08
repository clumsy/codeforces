q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = (int(i) for i in input().split())
    a, b = l1, r2 if l2 == l1 else l2
    print(a, b)
