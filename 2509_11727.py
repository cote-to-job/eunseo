mod =  10007
dp=[0,1,3]# 2*1 =1개 2*2= 2개 가가 세세
N=int(input())
for i in range(3,N+1):
    if i %2 : dp.append(dp[i-1]*2-1)
    else:dp.append(dp[i-1]*2+1)

print(dp[N]%mod)