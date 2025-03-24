def solution(numbers):
    answer = []
    
    for n in numbers:
        #짝수
        if n %2==0: answer.append(n+1)
        else: #홀수 
            bin_n='0'+ bin(n)[2:] #n 10->2로 변환  & 앞에 0을 붙여 111...일 시 0 찾을 수 있게 변경
            zero_idx = bin_n.rfind('0') # 작은 숫자부터 0 나오는 자리 찾기
            new_n = bin_n[:zero_idx]+ '10'+bin_n[zero_idx+2:]# 작은 수 부터 0을 1로 바꿈 -> 올림발생-> 1은 0으로
            answer.append(int(new_n,2))
            
        
    return answer