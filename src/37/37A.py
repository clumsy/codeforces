from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
cnt = Counter(a)
res = cnt.most_common()[0][1], len(cnt)
print(*res)
