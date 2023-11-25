a = int(input())
res = next(b for b in range(1, 21) if "8" in str(a + b))
print(res)
