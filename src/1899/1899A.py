t = int(input())
for _ in range(t):
    n = input()
    res = "Second" if sum(int(c) for c in n) % 3 == 0 else "First"
    print(res)
