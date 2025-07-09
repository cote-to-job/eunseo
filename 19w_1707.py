from collections import deque
import sys
input = sys.stdin.readline

def solve():
    global gr, adj, v

    gr = [-1] * (v + 1)

    for i in range(1, v + 1):
        if gr[i] != -1:
            continue

        q = deque()
        q.append(i)
        gr[i] = 0

        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if gr[nxt] != -1:
                    if gr[nxt] == gr[cur]:
                        return False
                    continue
                gr[nxt] = (gr[cur] + 1) % 2
                q.append(nxt)

    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    print("YES" if solve() else "NO")
