import sys
from collections import deque
 
input = sys.stdin.read
data = input().split()
idx = 0
T = int(data[idx])
idx += 1
directions = [(1,0), (0,1), (-1,0), (0,-1)]  # 하, 우, 상, 좌

for _ in range(T):
    m = int(data[idx])
    n = int(data[idx+1])
    k = int(data[idx+2])
    idx +=3
    
    grid = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x = int(data[idx])
        y = int(data[idx+1])
        idx +=2
        grid[y][x] = 1  # 좌표계 변환
        
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                # BFS 시작
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                
                while q:
                    cur = q.popleft()
                    for di, dj in directions:
                        ni = cur[0] + di
                        nj = cur[1] + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if not visited[ni][nj] and grid[ni][nj] == 1:
                                visited[ni][nj] = True
                                q.append((ni, nj))
                count += 1
    print(count)
