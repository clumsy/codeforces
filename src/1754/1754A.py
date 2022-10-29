t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    left = 0
    for c in s:
        if c == "Q":
            left += 1
        elif left > 0:
            left -= 1
    res = "Yes" if left == 0 else "No"
    print(res)
