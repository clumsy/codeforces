s = input()
names = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
res = "YES" if sum(s.count(name) for name in names) == 1 else "NO"
print(res)
