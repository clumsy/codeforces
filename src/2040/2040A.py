from collections import Counter


t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    cnt = Counter(i % k for i in a)
    res = next((k for k, v in cnt.items() if v == 1), None)
    if res is None:
        print("NO")
    else:
        print("YES")
        res = next(i + 1 for i, v in enumerate(a) if v % k == res)
        print(res)
