from collections import deque
# 내부는 접근 불가 밖에 있는것만 가능

def solution(storage, requests):
    answer=0
    container = [list(row) for row in storage]
        
    n, m = len(container), len(container[0]) 
    for req in requests:
        # 지게차 A
        if len(req) == 1:
            t = req[0]
            
            conn = [[False] * m for _ in range(n)]
            q = deque()
            for i in range(n):
                for j in range(m):
                    if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                        if container[i][j] == '.':
                            conn[i][j] = True
                            q.append((i, j))
            # BFS
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if container[nx][ny] == '.' and not conn[nx][ny]:
                            conn[nx][ny] = True
                            q.append((nx, ny))
            
            
            for i in range(n):
                for j in range(m):
                    if container[i][j] == t:
                        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                            container[i][j] = '.'
                        else:
                            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                                ni, nj = i + dx, j + dy
                                if 0 <= ni < n and 0 <= nj < m:
                                    if conn[ni][nj]:
                                        container[i][j] = '.'
                                        break
        
        # 크레인 BB
        elif len(req) == 2:
            t = req[0]  
            for i in range(n):
                for j in range(m):
                    if container[i][j] == t:
                        container[i][j] = '.'
    
                            
    for i in range(n):
        for j in range(m):
            if container[i][j] != '.':answer+=1
    return answer

solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])