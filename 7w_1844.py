from collections import deque

def solution(maps):
    w, h = len(maps[0]), len(maps)
    visit = [[0] * w for _ in range(h)]
    visit[0][0] = 1
    
    next = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for path in next:
            nx = x + path[0]
            ny = y + path[1]
            
            if (nx >= 0) and (ny >= 0) and (nx < h) and (ny < w):
                if (maps[x][y] == 1 and visit[nx][ny] == 0):
                    q.append((nx,ny))
                    visit[nx][ny] = visit[x][y] + 1
                
    return visit[h - 1][w - 1] or -1
