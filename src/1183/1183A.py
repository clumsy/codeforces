a = int(input())
for i in range(10):
    if sum(int(i) for i in str(a + i)) % 4 == 0:
        res = a + i
        break
print(res)
