'''
[1, 2, 3, 2, 3] 
 idx[0] 0이 나오는 경우 X 4
 idx[1]  <=2 으로 3
 idx[2] > idx[3] 으로 1
 idx[3] > idx[4] 로 1
 뒤에 나오는 숫자가 작으면 stop

'''

def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)) :
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: answer[i] +=1
            else :
                answer[i] +=1
                break
    
    
    return answer