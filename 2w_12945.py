#피보나치 수 fn + fn+1
def solution(n):
    f1,f2 =0,1
    for i in range(n):
        f1,f2 = f2,f1+f2
    
    return f1 % 1234567