from collections import deque

def solution(board):
    n = len(board)
    INF = float('inf')

    # 4방향
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # cost_map[x][y][d] = (x,y)에 d 방향으로 진입했을 때의 최소 비용
    cost_map = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    q = deque()

    # 출발 지점에서 첫 번째 이동은 하,우만 가능
    for d in (1, 2):
        nx, ny = dirs[d][0], dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            cost_map[nx][ny][d] = 100 #비용 초기화
            q.append((nx, ny, d))

    # BFS 
    while q:
        x, y, prev_d = q.popleft()
        curr_cost = cost_map[x][y][prev_d]

        for d, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy

            # 범위 & 벽 체크
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny] == 1:
                continue

            # 직진 +100, 코너 +600
            new_cost = curr_cost + (100 if d == prev_d else 600)

            # 방향별 최소 비용  
            if new_cost < cost_map[nx][ny][d]:
                cost_map[nx][ny][d] = new_cost
                q.append((nx, ny, d))

    # 도착점(n-1, n-1) 방향 중 최소값 반환
    return min(cost_map[n-1][n-1])
