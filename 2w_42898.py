#집0,0 ->학교(n,m)
def solution(m, n, puddles):
    mod = 1000000007

    # dp[y][x] 
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 집
    dp[1][1] = 1
    
    for i in range(1, n + 1):#u->d
        for j in range(1, m + 1):#l->r
            if [j, i] in puddles:  # 물에 잠긴 지역이면
                dp[i][j] = 0
                continue
            
            if i == 1 and j == 1:
                continue
            #down+ right방향
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod

    return dp[n][m]
print(solution(4,3,[[2,2]]))
