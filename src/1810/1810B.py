t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1 == 0:
        res = [-1]
    else:
        res = [int(i) + 1 for i in bin(n)[2:-1]]  # removing leading 0b and last digit
    if res != [-1]:
        print(len(res))
    print(*res)
