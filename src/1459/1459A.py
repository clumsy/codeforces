t = int(input())
for _ in range(t):
    n = int(input())
    r, b = (int(r) for r in input()), (int(b) for b in input())
    diff = sum(0 if r == b else (r - b) // abs(r - b) for r, b in zip(r, b))
    res = "RED" if diff > 0 else "BLUE" if diff < 0 else "EQUAL"
    print(res)
