t = int(input())
for i in range(t):
    n, s = int(input()), input()
    cnt = [0] * 3
    for c in s.split("0"):
        if c:
            k = len(c)
            cnt[2 if k == 2 else 1 if k & 1 == 1 else 0] += 1
    res = (
        "NO"
        if cnt[1] & 1 == 1 or (cnt[2] == 1 and cnt[1] < 2 and cnt[0] < 1)
        else "YES"
    )
    print(res)
