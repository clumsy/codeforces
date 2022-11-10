n = int(input())
b = 0
for _ in range(n):
    m, c = (int(i) for i in input().split())
    b += 1 if m > c else -1 if m < c else 0
res = "Mishka" if b > 0 else "Chris" if b < 0 else "Friendship is magic!^^"
print(res)
