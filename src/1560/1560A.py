from itertools import count, islice

t = int(input())
for _ in range(t):
    k = int(input())
    gen = (i for i in count(start=1) if i % 3 != 0 and i % 10 != 3)
    res = next(islice(gen, k - 1, None))
    print(res)
