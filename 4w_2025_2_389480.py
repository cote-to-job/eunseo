#info[i][0]개의 A에 흔적 남김 ->누적 n이상이면 잡힘
#info[i][1]개의 B에 흔적 남김 ->누적 m이상이면 잡힘
#A,B몯두 경찰에 잡히지 않도록 물건 훔침&  A도둑의 흔적 최솟값
def solution(info, n, m): 
    # dp는 (현재 A,B 누적)
    dp = {(0, 0)}
    
     
    for a_item, b_item in info:
        next_dp = set()
        for a_trace, b_trace in dp:
            # 1. A 도둑이 물건을 훔치는 경우
            new_a = a_trace + a_item
            if new_a < n:  # A의 누적 흔적이 n 미만이어야 함
                next_dp.add((new_a, b_trace))
            
            # 2. B 도둑이 해당 물건을 훔치는 경우
            new_b = b_trace + b_item
            if new_b < m:  # B의 누적 흔적이 m 미만이어야 함
                next_dp.add((a_trace, new_b))
        dp = next_dp
        # valid한 상태가 없다면 실패
        if not dp:
            return -1

    # A의 누적 흔적이 최소인 값을 반환
    a_min=120 #a최대값 설정
    for a,b in dp:
        a_min = min(a, a_min)
    return a_min
