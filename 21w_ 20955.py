import sys
input = sys.stdin.read

def find(x):
    root = x
    while parent[root] >= 0:
        root = parent[root]
    while x != root:
        next_x = parent[x]
        parent[x] = root
        x = next_x
    return root

def try_merge(u, v):
    global cnt
    u = find(u)
    v = find(v)
    if u == v:
        cnt += 1
        return
    if parent[u] > parent[v]:
        u, v = v, u
    parent[u] += parent[v]
    parent[v] = u

data = input().split()
n = int(data[0])
m = int(data[1])
parent = [-1] * (n + 1)
cnt = 0

index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    try_merge(u, v)
    index += 2
 
print(n - m - 1 + 2 * cnt)
