import sys
from collections import defaultdict


def dfs(x, y, cur_str):
    result[cur_str] += 1
    if len(cur_str) == 5:
        return
    for i in range(8):
        nx, ny = (x + dx[i]) % n, (y + dy[i]) % m
        dfs(nx, ny, cur_str + board[nx][ny])


input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
targets = [input().rstrip() for _ in range(k)]

result = defaultdict(int)

for i in range(n):
    for j in range(m):
        dfs(i, j, board[i][j])

for t in targets:
    print(result[t])