def count(s):
    cnt = x = y = 0
    for c in s:
        x += 1 if c == "R" else -1 if c == "L" else 0
        y += 1 if c == "D" else -1 if c == "U" else 0
        cnt += x == 0 and y == 0
    return cnt


n, s = int(input()), input()
res = sum(count(s[i:]) for i in range(len(s)))
print(res)
