t = int(input())
for _ in range(t):
    s = input()
    res, round, square = 0, 0, 0
    for c in s:
        round += c == "("
        square += c == "["
        if c == ")" and round > 0:
            round -= 1
            res += 1
        if c == "]" and square > 0:
            square -= 1
            res += 1
    print(res)
