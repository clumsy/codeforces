a, b, c = sorted(int(i) for i in input().split())
res = "check again" if c - a >= 10 else f"final {b}"
print(res)
