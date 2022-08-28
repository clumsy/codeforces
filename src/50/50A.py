m, n = (int(i) for i in input().split())
# if no more than one odd - whole board is used, else one square remains unoccupied
print(m * n // 2)
