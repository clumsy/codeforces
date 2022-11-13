n, s = int(input()), input()
a = s.count("A")
res = "Anton" if 2 * a > n else "Danik" if 2 * a < n else "Friendship"
print(res)
