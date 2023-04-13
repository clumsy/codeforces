board = [[c for c in input()] for _ in range(8)]
value = {
    "q": 9,
    "r": 5,
    "b": 3,
    "n": 3,
    "p": 1,
    "k": 0,
}
diff = 0
for r in range(8):
    for c in range(8):
        v = board[r][c]
        if v != ".":
            cur = 1 if v.isupper() else -1
            cur *= value[v.lower()]
            diff += cur
res = "Draw" if diff == 0 else "White" if diff > 0 else "Black"
print(res)
