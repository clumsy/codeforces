with open("input.txt") as f:
    input = f.readlines()
n, k = (int(i) for i in input[0].split())
a = [int(i) for i in input[1].split()]
order = sorted(range(n), key=a.__getitem__)
res = a[order[n - k]], sorted(i + 1 for i in order[n - k :])
with open("output.txt", "w") as f:
    print(res[0], file=f)
    print(*res[1], file=f)
