a, b, c = (int(i) for i in input().split())
# a * c to download will take a * c / b seconds
# a * c = b * (c + t)
# t = a * c / b - c = (a * c - b * c) / b = c * (a - b) / b
res = max((c * (a - b) + b - 1) // b, 0)
print(res)
