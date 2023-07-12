from collections import Counter

n = int(input())
cnt = Counter(int(input()) for _ in range(n))
res = cnt.keys() if len(cnt) == 2 and 2 * cnt[next(iter(cnt.keys()))] == n else []
if res:
    print("YES")
    print(*res)
else:
    print("NO")
