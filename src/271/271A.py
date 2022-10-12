from collections import Counter

y = int(input())
while True:
    y += 1
    if all(v == 1 for _, v in Counter(str(y)).items()):
        res = y
        break
print(res)
