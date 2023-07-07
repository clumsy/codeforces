from collections import Counter, deque

n, p = int(input()), [int(i) - 1 for i in input().split()]
in_deg = Counter(p)
q = deque(i for i in range(n) if in_deg[i] == 0)
# all person in a cycle will have self as the value
# otherwise we point towards this cycle
ans = {i: i for i in range(n)}
while q:
    cur = q.pop()
    in_deg[p[cur]] -= 1
    # this person is not in a cycle so we point towards it
    ans[cur] = p[cur]
    if in_deg[p[cur]] == 0:
        q.appendleft(p[cur])


def res(i):
    if i != ans[i]:
        ans[i] = res(p[i])
    return ans[i]


res = [res(i) + 1 for i in range(n)]
print(*res)
