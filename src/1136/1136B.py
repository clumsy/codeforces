n, k = (int(i) for i in input().split())
# she will finish at either first or last position
# 1st turn throw the stop to that last position (it will have 2 stones)
# all other steps always throw stones to the k-th position
# in total n + 1 steps to throw stones
# she will have to open all n manholes, so another n steps
# now it's just the movement, she will first go the the closest end
# and then all the way back
res = (n + 1) + n + n - 1 + min(k - 1, n - k)
print(res)
