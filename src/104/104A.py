n = int(input())
n -= 10  # we have a queen of spades
if 0 < n < 10 or n == 11:
    res = 4  # 4x(2-9, A)
elif n == 10:
    res = 15  # 4x10, 4xJ, 3xQ, 4xK
else:
    res = 0
print(res)
