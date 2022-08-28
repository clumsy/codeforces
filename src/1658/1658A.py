t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    need, between = 0, 2
    for i in range(n):
        if s[i] == "1":
            between += 1  # remember how many females between males
        else:
            need += max(2 - between, 0)  # should be at least 2
            between = 0
    print(need)
