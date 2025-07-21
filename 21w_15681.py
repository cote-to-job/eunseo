import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
adj = [[] for _ in range(N + 1)]
subtree_size = [0] * (N + 1)
visited = [False] * (N + 1)

# 인접리스트
for _ in range(N - 1):
    U, V = map(int, input().split())
    adj[U].append(V)
    adj[V].append(U)

# DFS 
def count_subtree_nodes(cur):
    visited[cur] = True
    for nxt in adj[cur]:
        if not visited[nxt]:
            subtree_size[cur] += count_subtree_nodes(nxt)
    subtree_size[cur] += 1
    return subtree_size[cur]

count_subtree_nodes(R)
 
for _ in range(Q):
    q = int(input())
    print(subtree_size[q])
