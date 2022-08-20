t = int(input())
for _ in range(t):
    n = int(input())
    # first round: all sums are odd, odds are smaller - they advance
    # second round onwards: only odd numbers remain, sum always even, eventually max odd number wins
    res = 2**n - 1
    print(res)
