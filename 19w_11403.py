from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0]*n

    while queue:
        q = queue.popleft()
        for i in range(n):
            if not check[i] and graph[q][i]:
                check[i] = 1
                visited[x][i] = 1
                queue.append(i)

for i in range(n):
    bfs(i)

for row in visited:
    print(*row)
