n = int(input())
for _ in range(n):
    c1, c2 = input()
    print((ord(c1) - ord("a")) * 25 + (ord(c2) - ord("a")) + (1 if c1 > c2 else 0))
