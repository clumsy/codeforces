from collections import Counter

n, a = int(input()), Counter(int(i) for i in input().split())
res = n - sum(1 <= i <= n for i in a)
print(res)
