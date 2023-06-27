from collections import Counter

n, a = int(input()), (int(i) for i in input().split())
cnt = Counter(a)
res = (
    ([5] * (9 * (cnt[5] // 9)) + [0] * cnt[0])
    if cnt[5] >= 9 and cnt[0] > 0
    else [0]
    if cnt[0] > 0
    else [-1]
)
res = "".join(str(i) for i in res)
print(res)
