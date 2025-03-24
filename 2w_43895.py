'''
2번 (-는 0으로 X)
nn(11*n) n+n =2n , n/n=1 , n*n = n**2

3번 사용
nnn(111*n)  
nn+n 12*n  nn-n=10*n nn/n=11 nn*n =11*n*n 
2n+n = 3n 2n/n=2 2n*n = 2*n**2 
n*n-n 
'''
#N과 사칙연산만 사용해서 표현 --> 최소한의 N만 사용

def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i)) # N,NN,NNN
        
        for j in range(1,i):
            # N사용횟수 n1 <=n2
            for n1 in dp[j]: 
                for n2 in dp[i-j]:
                    dp[i].add(n1+n2)
                    dp[i].add(n1-n2)
                    dp[i].add(n1*n2)
                    if n2 !=0: dp[i].add(n1//n2)
        
        if number in dp[i]: return i
    return -1
    


solution(5,12)
