
    #x,y좌표인 points =>n,
    #routes =>m 으로 points의 순번 중 하나를 가게됨
    #r개의 로봇이 동시 출발해서 +-x,+-y중 하나로 이동
    #최단경로로 이동하며 같을 때 x가 먼저
    
    # 같은 좌표에 로봇이 2대 이상 모인다면 충돌 & 충돌 횟수
def solution(points, routes):
    # sign 함수: 방향 판별용
    def sign(x):
        if x>0: return 1
        elif x<0 :return  -1
        else:return 0
        
    # 1) 각 로봇별로 초 단위 위치 리스트
    all_paths = []
    for route in routes:
        # route: 방문할 포인트 번호들의 리스트
        # 시작 위치: 첫 번째 포인트
        r0, c0 = points[route[0] - 1]
        path = [(r0, c0)]  # t=0 위치

        # 다음 포인트까지 최단 경로로 이동
        for pid in route[1:]:
            rt, ct = points[pid - 1]
            # 현재 위치에서 목표 위치로 한 칸씩 이동
            while (r0, c0) != (rt, ct):
                # r좌표 우선 이동
                if r0 != rt:
                    r0 += sign(rt - r0)
                else:
                    c0 += sign(ct - c0)
                path.append((r0, c0))
        all_paths.append(path)

    # 2)  t=0부터 모든 로봇이 완료될 때까지
    answer = 0
    max_t = max(len(p) for p in all_paths)
    for t in range(max_t):
        counter = {}
        # 각 로봇이 t초에 어디에 있는지 
        for path in all_paths:
            if t < len(path):
                coord = path[t]
                counter[coord] = counter.get(coord, 0) + 1
        # 위험 상황: 같은 좌표에 2대 이상 모인 경우, 좌표별로 1회씩 카운트
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1

    return answer
