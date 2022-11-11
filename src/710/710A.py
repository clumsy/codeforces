king = input()
row, col = int(king[1]) - 1, ord(king[0]) - ord("a")
res = 3 if row % 7 == 0 and col % 7 == 0 else 5 if row % 7 == 0 or col % 7 == 0 else 8
print(res)
