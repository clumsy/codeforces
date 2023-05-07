n, a = int(input()), (int(i) for i in input().split())
even, odd = [], []
for i in a:
    (odd if i & 1 else even).append(i)
even.sort(reverse=True)
odd.sort(reverse=True)
size = min(len(even), len(odd))
even = even[min(size + 1, len(even)) :]
odd = odd[min(size + 1, len(odd)) :]
res = sum(even) + sum(odd)
print(res)
