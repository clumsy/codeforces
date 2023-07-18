a, b = (input() for _ in range(2))
res = -1 if a == b else max(len(a), len(b))
print(res)
