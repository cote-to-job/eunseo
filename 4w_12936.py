
import math

def solution(n, k):
    numbers = [i for i in range(1, n+1)]
    k -= 1  # 0-index
    answer = []
    
    # 각 자리마다 팩토리얼 값을 활용하여 숫자 선택
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1) # (n-1)!,(n-2)!,...,2!,1!,0! = 1 
        index = k // fact #n=5 k =10, 9//24->0-1 | 9//6 ->1-3 | 245 3//2->1-4 | 1//1->1-5
        answer.append(numbers.pop(index))
        k %= fact # 9%24 -> 9%6 ->3%2 ->1%1->0
        
    return answer
solution(5,10)
'''
from itertools import permutations 
def solution(n, k): 
    num_li = [i for i in range(1,n+1) ] 
    answer = list(permutations(num_li,n))[k-1]
    return answer

#시간초과 63.2 어떻게 해결?
n*(n-1)*(n-2)...

k = n! 

'''