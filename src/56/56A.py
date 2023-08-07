n = int(input())
drinks = {
    "ABSINTH",
    "BEER",
    "BRANDY",
    "CHAMPAGNE",
    "GIN",
    "RUM",
    "SAKE",
    "TEQUILA",
    "VODKA",
    "WHISKEY",
    "WINE",
}
res = 0
for _ in range(n):
    s = input()
    if all(c.isdigit() for c in s):
        res += int(s) < 18
    else:
        res += s in drinks
print(res)
