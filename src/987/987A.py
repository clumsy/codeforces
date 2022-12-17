gems = {
    "purple": "Power",
    "green": "Time",
    "blue": "Space",
    "orange": "Soul",
    "red": "Reality",
    "yellow": "Mind",
}
n = int(input())
s = (input() for _ in range(n))
missing = set(gems.keys()).difference(s)
print(len(missing))
for g in missing:
    print(gems[g])
