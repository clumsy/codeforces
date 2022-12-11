k, r = (int(i) for i in input().split())
for res in range(1, 11):
    if res * k % 10 in {0, r}:
        break
print(res)
