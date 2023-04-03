n = int(input())
cnt = [0] * 7
res = 0
for _ in range(n):
    for i, c in enumerate(input()):
        cnt[i] += c == "1"
        res = max(res, cnt[i])
print(res)
