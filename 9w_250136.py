from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0]) 
    fuel  = [[0]*m for _ in range(n)]
    sizes = {}
    cnt   = 0  
    dir  = [(-1,0),(1,0),(0,-1),(0,1)]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and fuel[i][j] == 0:
                cnt += 1
                q, fuel[i][j] = deque([(i,j)]), cnt
                size = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in dir:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and fuel[nx][ny] == 0:
                            fuel[nx][ny] = cnt
                            size += 1
                            q.append((nx, ny))
                sizes[cnt] = size


    for j in range(m):
        seen  = set()
        total = 0
        for i in range(n):
            fuel_id = fuel[i][j]
            if fuel_id and fuel_id not in seen:
                seen.add(fuel_id)
                total += sizes[fuel_id]
        answer = max(answer, total)

    return answer