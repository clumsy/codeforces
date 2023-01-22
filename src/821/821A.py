from collections import Counter

n = int(input())
lab = [[int(i) for i in input().split()] for _ in range(n)]
rows = [Counter(lab[r]) for r in range(n)]
cols = [Counter(lab[r][c] for r in range(n)) for c in range(n)]
res = "YES"
for r in range(n):
    if res == "NO":
        break
    for c in range(n):
        v = lab[r][c]
        if v == 1:
            continue
        rows[r][v] -= 1
        cols[c][v] -= 1
        found = False
        for i, cnt in rows[r].items():
            if cnt > 0 and cols[c].get(v - i, 0) > 0:
                found = True
                break
        if not found:
            res = "NO"
            break
        rows[r][v] += 1
        cols[c][v] += 1
print(res)
