t = int(input())
for _ in range(t):
    n = int(input())
    print(f"{n} {' '.join(str(i) for i in range(1, n))}")
