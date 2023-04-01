n = int(input())
for _ in range(n):
    x = int(input())
    res = "NO"
    b = x // 7
    while b >= 0:
        a = (x - b * 7) // 3
        if x == a * 3 + b * 7:
            res = "YES"
            break
        b -= 1
    print(res)
