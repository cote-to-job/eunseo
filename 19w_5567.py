from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
dist = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = 0
q = deque()
q.append(1)
dist[1] = 1

while q:
    cur = q.popleft()
    if dist[cur] > 3:  # 친구의 친구까지만 카운트 (dist 2: 친구, dist 3: 친구의 친구)
        continue
    for nxt in adj[cur]:
        if dist[nxt] == 0:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
            if dist[nxt] <= 3 and nxt != 1:  # 1번 제외
                ans += 1

print(ans)
