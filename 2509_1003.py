'''피보나치 수열 0+1 1+1  2+1 3+2 3+5 


def fibo(n,z_cnt,o_cnt):
    if (n==0):
        z_cnt +=1
        return 0
    elif (n==1):
        o_cnt+=1
        return 1
    else :
        return fibo(n-1)+ fibo(n-2)
    
'''
# 0과 1이 몇 번 출력?

n = int(input())
fibo = [[0,0] for _ in range(41)]

fibo[0][0] = 1
fibo[1][1] = 1

for i in range(2,41):
    
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]


for _ in range(n):
    
    i=int(input())
    print(fibo[i][0], fibo[i][1])