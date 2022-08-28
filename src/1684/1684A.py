t = int(input())
for _ in range(t):
    n = input()
    if len(n) == 2:
        print(n[1])
    else:
        print(min(n))
