a, b, c, d = (int(i) for i in input().split())
misha = max(3 * a // 10, a - a * c // 250)
vasya = max(3 * b // 10, b - b * d // 250)
res = "Tie" if misha == vasya else "Vasya" if vasya > misha else "Misha"
print(res)
