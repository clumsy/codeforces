t = int(input())
for _ in range(t):
    input()
    a = [int(i) for i in input().split()]
    odd = sum(1 for i in a if i & 1 == 1)
    # the minority of odd or even has to be removed completely
    print(min(odd, len(a) - odd))
