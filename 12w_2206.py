import sys
from collections import deque 
    
def bfs():
    dist = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 1  # 시작 지점 거리 1
    q = deque()
    q.append((0, 0, 0))
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y, broken = q.popleft()
        
        # 도착 시 거리 반환
        if x == n-1 and y == m-1:
            return dist[x][y][broken]
        
        next_dist = dist[x][y][broken] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 방문 안 한 경우
                if board[nx][ny] == '0' and dist[nx][ny][broken] == -1:
                    dist[nx][ny][broken] = next_dist
                    q.append((nx, ny, broken))
                
                # 벽을 부수고 이동하는 경우
                elif board[nx][ny] == '1' and not broken and dist[nx][ny][1] == -1:
                    dist[nx][ny][1] = next_dist
                    q.append((nx, ny, 1))
    
    return -1
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]    
print(bfs())

