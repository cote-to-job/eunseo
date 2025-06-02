'''
문제
총 25명의 여학생들로 이루어진 여학생반은 5×5의 정사각형 격자 형태로 자리가 배치되었고, 얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다. 곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.

위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. ‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.

이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.

입력
'S'(이다‘솜’파의 학생을 나타냄) 또는 'Y'(임도‘연’파의 학생을 나타냄)을 값으로 갖는 5*5 행렬이 공백 없이 첫째 줄부터 다섯 줄에 걸쳐 주어진다.

출력
첫째 줄에 ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 출력한다.

예제 입력 1 
YYYYY
SYSYS
YYYYY
YSYYS
YYYYY
예제 출력 1 
2
'''
from itertools import combinations
from collections import deque

# 5x5 
board = [input() for _ in range(5)]
answer = 0
pos =[]
#7명의 여학생들로 구성
for comb in combinations(range(25), 7):
    for i in comb:
        pos.append((i//5,i%5))
    s_count = sum(board[x][y] == 'S' for x, y in pos)
    if s_count < 4:
        continue
    
    # BFS로 연결 상태 확인
    start = pos[0]
    visited = set([start])
    q = deque([start])
    pos_set = set(pos)
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 상하좌우 탐색
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) in pos_set and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))
    
    # 모든 7명이 연결된 경우만 카운트
    if len(visited) == 7:
        answer += 1

print(answer)