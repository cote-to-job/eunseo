#같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가
#이용자가 n x m명 이상 (n + 1) x m명 미만이라면 최소 n대의 증설된 서버가 운영 중
# 한 번 증설한 서버는 k시간 동안 운영-> 반납합니다.
def solution(players, m, k):
    answer = 0             
    dp = [0] * 24               

    for i in range(24):
        # 현재 시간 i에 필요한 추가 서버 수
        required = players[i] // m
        # 이미 활성화된 추가 서버 수와 비교하여 부족하면 추가 증설
        if dp[i] < required:
            add = required - dp[i]
            answer += add
            # 추가한 서버는 시간 i부터 i+k-1까지 운영
            for j in range(i, min(i+k, 24)):
                dp[j] += add
        
            
    return answer
