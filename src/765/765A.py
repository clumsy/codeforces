n, home = int(input()), input()
res = 0
for _ in range(n):
    res += 1 - 2 * input().startswith(home)
res = "home" if res == 0 else "contest"
print(res)
