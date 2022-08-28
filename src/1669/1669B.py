from collections import defaultdict


t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    c, res = defaultdict(int), -1
    for i in a:
        c[i] += 1
        if c[i] == 3:
            res = i
            break
    print(res)
