first, last = input().split()
i = 1
while i < len(first) and first[i] < last[0]:
    i += 1
res = first[:i] + last[0]
print(res)
