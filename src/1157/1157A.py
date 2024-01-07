n = int(input())
n, r = divmod(n, 10) if n > 9 else (n, 10)
res = 9 + (
    10 - r
)  # 1,2,3,4,5,6,7,8,9 are always reachable, if n has 10 at the end we count this
n += 1
while True:
    while n % 10 == 0:
        n //= 10
    if n < 10:
        break
    n, r = divmod(n, 10)
    res += 10 - r
    n += 1
print(res)
